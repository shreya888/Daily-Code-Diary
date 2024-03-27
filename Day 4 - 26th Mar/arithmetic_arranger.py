def arithmetic_arranger(problems, show_answers=False):
    """
    Arranges arithmetic problems vertically and optionally shows the answers.

    Args:
        problems (list): List of strings representing arithmetic problems.
        show_answers (bool, optional): Flag to indicate whether to display answers. Defaults to False.

    Returns:
        str: String containing the arranged arithmetic problems and optionally their answers.

    Example:
        "235 + 52" becomes:
          235
        +  52
        -----
    """
    # Check if there are more than 5 problems
    if len(problems) > 5:
        return('Error: Too many problems.')
    
    # Initialize variables for arranged problems
    spaces = 4
    arranged_problems = []
    top_row = ''
    bot_row = ''
    dashes  = ''
    ans_row = ''
    
    # Iterate through each problem
    for i in range(len(problems)):
        f, o, s = problems[i].split(' ')
        
        # Check if the operator is '+' or '-'
        if o != '+' and o != '-':
            return ("Error: Operator must be '+' or '-'.")
        
        # Check if numbers contain only digits
        if not (f.isdigit() and s.isdigit()):
            return ('Error: Numbers must only contain digits.')
        
        # Check if numbers are more than four digits
        if int(f)//10000 > 0 or int(s)//10000:
            return ('Error: Numbers cannot be more than four digits.')
        
        # Determine the number of digits in the longest operand
        digits = max(len(f), len(s))
        
        # Arrange the top and bottom rows of the problem
        top_row += f.rjust(digits+2) 
        bot_row += o + s.rjust(digits+1)
        dashes += '-'*(digits+2)
        
        # Add spaces between problems
        if i < len(problems)-1:
            top_row += ' '*spaces
            bot_row += ' '*spaces
            dashes += ' '*spaces
        
        # Construct the complete arranged problems string
        arranged_problems = top_row+'\n'+bot_row+'\n'+dashes
        
        # Add answers if show_answers is True
        if show_answers:
            if o == '+':
                ans = str(int(f)+int(s))
            else:
                ans = str(int(f)-int(s))
            ans_row += ans.rjust(digits+2)
            if i < len(problems)-1:
                ans_row +=' '*spaces
            arranged_problems += '\n' + ans_row

    return arranged_problems

# Example test
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
