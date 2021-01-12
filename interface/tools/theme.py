class Theme:
    main_background = (
        'background-color : #17181c;'
    )

    cellule = (
        'QLineEdit {'
            'color: #242424;'
            'font-size: 20pt;'
            'background-color :white;'
            'border: none'
        '}'
       
        'QLineEdit::hover {'
            'background-color : #e6e6e6;'
            'cursor: pointer;'
        '}'
        
        'QLineEdit::focus {' 
            'background-color: #009c43'
        '}'
    )

    indice = (
        'background-color: white;'
        'color: #3d3d3d'
        'display: none !important'
    )

    button = (
        'QPushButton {'
            'color: #fff;'
            'background-color: #6c757d;'
            'border-color: #6c757d;'
            'border-radius: 5px;'
            'font-size: 20pt;'
            'height: 60px;'
        '}'

        'QPushButton:hover {'
            'background-color: #535b61;'
        '}'

        'QPushButton:pressed {'
            'background-color: #4c5359;'
        '}'
    )
