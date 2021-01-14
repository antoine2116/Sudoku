class Theme:
    main_background = (
        'background-color : #17181c;'
    )

    cellule_valeur = (
        'QLineEdit {'
            'color: #242424;'
            'font-size: 20pt;'
            'background-color :white;'
            'border: none;'
        '}'
       
        'QLineEdit::hover {'
            'background-color : #e6e6e6;'
        '}'
    )

    cellule_valeur_focused = (
        'QLineEdit {'
            'border: none;'
            'background-color : #a4d0fc !important;'
        '}'

        'QLineEdit::hover {'
            'background-color : #75a3d1 !important;'
        '}'
    )

    cellule_indice_focused = (
        'QLineEdit {'
            'border: none;'
            'background-color : #a4d0fc !important;'
        '}'
    )

    cellule_indice = (
        'QLineEdit {'
            'background-color: white;'
            'color: #3d3d3d;'
            'border: none;'
        '}'
    )

    button = (
        'QPushButton {'
            'color: #fff;'
            'background-color: #6c757d;'
            'border-color: #484e54;'
            'border-radius: 5px;'
            'font-size: 18pt;'
            'height: 50px;'
        '}'

        'QPushButton:hover {'
            'background-color: #535b61;'
        '}'

        'QPushButton:pressed {'
            'background-color: #4c5359;'
        '}'
    )

    button_indice = (
        'QPushButton {'
            'font-size: 13pt !important;'
        '}'
    )

    button_indice_selected = (
        'QPushButton {'
            'background-color: #24537d;'
        '}'

        'QPushButton:hover {'
            'background-color: #1d5f99;'
        '}'

        'QPushButton:pressed {'
            'background-color: #1267b3;'
        '}'
    )
