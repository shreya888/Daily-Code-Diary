# Imports
import torch
import torch.nn as nn  # All neural network components/modules, nn.Linear, nn.Conv2d, BatchNorm, Loss Function
import torch.optim as optim  # For all optimization algorithms, SGD, Adam, etc.
import torchvision
import torchvision.datasets as datasets  # Has standard datasets we can import nicely
import torchvision.transforms as transforms  # Transformations we can perform on our dataset
from torch.utils.data import DataLoader  # Easier to manage dataset and creates mini-batches
from torch.utils.tensorboard import SummaryWriter  # To print to tensorboard
from FC_GAN import Discriminator, Generator

# Hyperparameters
device = "cuda" if torch.cuda.is_available() else "cpu"  # Set device
lr = 3e-4
z_dim = 64
image_dim = 28 * 28 * 1  # for MNIST, = 784
batch_size = 32
num_epochs = 50

# Initialize network(s)
gen = Generator(z_dim, image_dim).to(device)
disc = Discriminator(image_dim).to(device)

# Using fixed noise to see how changes happen across epochs by visualizing via Tensorboard
fixed_noise = torch.randn((batch_size, z_dim)).to(device)
transforms = transforms.Compose(
    [transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))]
)

# Load Data
datasets = datasets.MNIST(root="dataset/", transform=transforms, download=True)
loader = DataLoader(datasets, batch_size=batch_size, shuffle=True)

# Optimizer and Loss
opt_disc = optim.Adam(disc.parameters(), lr=lr)
opt_gen = optim.Adam(gen.parameters(), lr=lr)
criterion = nn.BCELoss()

# Tensorboard summary writer for both fake and real
writer_fake = SummaryWriter(f"logs/fake")
writer_real = SummaryWriter(f"logs/real")
step = 0

for epoch in range(num_epochs):
    for batch_idx, (real, _) in enumerate(loader):
        real = real.view(-1, 784).to(device)  # Get data to cuda if possible
        batch_size = real.shape[0]

        # Train Discriminator: max log(D(real)) + log(1 + D(G(z)))
        # forward
        noise = torch.randn(batch_size, z_dim).to(device)
        fake = gen(noise)
        disc_real = disc(real).view(-1)
        lossD_real = criterion(disc_real, torch.ones_like(disc_real))  # because real so target is 1
        disc_fake = disc(fake).view(-1)
        lossD_fake = criterion(disc_fake, torch.zeros_like(disc_fake))  # because fake so target is 0
        lossD = (lossD_real + lossD_fake) / 2
        # backward
        disc.zero_grad()
        lossD.backward(retain_graph=True)
        opt_disc.step()

        # Train Generator min(log(1 - D(G(z))) <--> max log(D(G(z)))
        # forward
        output = disc(fake).view(-1)
        lossG = criterion(output, torch.ones_like(output))
        # backward
        gen.zero_grad()
        lossG.backward()
        opt_gen.step()

        # Plot things to tensorboard
        if batch_idx == 0:
            print(
                f"Epoch [{epoch}/{num_epochs}] Batch {batch_idx}/{len(loader)} \
                              Loss D: {lossD:.4f}, Loss G: {lossG:.4f}"
            )

            with torch.no_grad():
                fake = gen(fixed_noise).reshape(-1, 1, 28, 28)
                data = real.reshape(-1, 1, 28, 28)
                img_grid_fake = torchvision.utils.make_grid(fake, normalize=True)
                img_grid_real = torchvision.utils.make_grid(data, normalize=True)
                writer_fake.add_image(
                    "Mnist Fake Images", img_grid_fake, global_step=step
                )
                writer_real.add_image(
                    "Mnist Real Images", img_grid_real, global_step=step
                )
                step += 1  # When add one datapoint, it will move 1 step

