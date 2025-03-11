"""
    Banner module
"""
        
        
def banner(nchar=80, char="=", title=None, padding=0):
    """Creates a formatted banner with optional centered title.
    
    This function prints a text banner for visual separation in terminal output.
    It can display a centered title and allows customization of character length
    and border character.
    
    Args:
        nchar: Integer specifying the total width of the banner. Defaults to 80.
        char: String character used for the banner border. Defaults to "=".
        title: Optional string to display centered in the banner. If None, only
            the border lines are printed. Defaults to None.
        padding: Number of spaces to add before and after the title text on the same line.
            Defaults to 0.
            
    Returns:
        None
        
    Examples:
        >>> banner(40, "-", "RESULTS")
        ----------------------------------------
                       RESULTS                  
        ----------------------------------------
        
        >>> banner(30, "#")
        ##############################
    """
    # Input validation
    nchar = max(1, int(nchar))  # Ensure nchar is at least 1 and an integer
    char = str(char)[0]  # Take only the first character if multiple provided
    padding = max(0, int(padding))  # Ensure padding is non-negative and an integer
    
    border = char * nchar
    print(border)
    
    if title is not None:
        # Calculate available space for title
        avail_space = nchar - (2 * padding)
        
        if len(title) > avail_space:
            # Truncate with ellipsis if title is too long
            title = title[:avail_space - 3] + "..."
        
        # Create padded title line
        padded_title = " " * padding + title + " " * padding
        print(padded_title.center(nchar))
        print(border)