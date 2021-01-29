class Style:
    """
    Object that contains all the stytling propeties used through the soduku
    """

    # region Global
    main_background = (
        'background-color : #17181c;'
    )

    menu_bar = (
        'QMenuBar {'
        'background-color : #858585;'
        '}'
        'QMenu {'
        'background-color : #858585;'
        '}'
    )

    home_logo = (
        'QLabel {'
        'margin-top: 30px;'
        '}'
    )
    # endregion

    # region Home
    home_title = (
        'QLabel {'
        'font-size: 50pt;'
        'color: white;'
        'margin: 30px 150px 80px 150px;'
        '}'
    )

    home_label = (
        'QLabel {'
        'font-size: 18pt;'
        'color: white;'
        '}'
    )

    home_button = (
        'QPushButton {'
        'color: #4a4a4a;'
        'background-color: #9cb8ff;'
        'border-color: #484e54;'
        'border-radius: 5px;'
        'font-size: 18pt;'
        'height: 60px;'
        '}'

        'QPushButton:hover {'
        'background-color: #7a9efa;'
        '}'

        'QPushButton:pressed {'
        'background-color: #6d94f7;'
        '}'
    )

    combo_file = (
        'QComboBox {'
        'font-size: 18pt;'
        'color: black;'
        'background-color: white;'
        'selection-background-color: #6c757d;'
        '}'

        'QListView {'
        'color: black;'
        'background-color: white;'
        '}'
    )
    # endregion

    # region Cells
    # Cell Value
    cell_value = (
        'QLineEdit {'
        'color: #1c56e6;'
        'font-size: 17pt;'
        'background-color :white;'
        'border: none;'
        '}'

        'QLineEdit::hover {'
        'background-color : #e6e6e6;'
        '}'
    )

    cell_value_checked = (
        'QLineEdit {'
        'color: #078747;'
        '}'
    )

    cell_value_fixed = (
        'QLineEdit {'
        'color: #242424 !important;'
        '}'
    )

    cell_value_selected = (
        'QLineEdit {'
        'border: none;'
        'background-color : #d6d6d6 !important;'
        '}'

        'QLineEdit::hover {'
        'background-color : #c4c2c2 !important;'
        '}'
    )

    # Cell hint
    cell_hint = (
        'QLineEdit {'
        'background-color: white;'
        'color: #1c56e6;'
        'border: none;'
        '}'
    )

    cell_hint_selected = (
        'QLineEdit {'
        'border: none;'
        'background-color : #d6d6d6 !important;'
        '}'
        
        'QLineEdit::hover {'
        'background-color : #d6d6d6 !important;'
        '}'
    )
    # endregion

    # region Controls Panel
    # Controls buttons
    controls_button = (
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

    controls_button_smaller = (
        'QPushButton {'
        'font-size: 13pt !important;'
        '}'
    )

    controls_button_delete = (
        'QPushButton {'
        'color: #1c1c1c;'
        'font-size: 30pt;'
        'background-color: #d64040;'
        '}'

        'QPushButton:hover {'
        'background-color: #c73232;'
        '}'

        'QPushButton:pressed {'
        'background-color: #c92828;'
        '}'
    )

    controls_button_enabled = (
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

    # Timer
    timer_button = (
        'QPushButton {'
        'background-color : #9cb8ff;'
        'border-color: #484e54;'
        'border-radius: 5px;'
        'font-size: 18pt;'
        'height: 50px;'
        '}'

        'QPushButton:hover {'
        'background-color: #6d8ee3;'
        '}'

        'QPushButton:pressed {'
        'background-color: #5a7bd1;'
        '}'
    )

    timer_label = (
        'font-size: 30pt;'
        'color: white;'
    )
    # endregion

    # region Popup
    popup = (
        'QInputDialog {'
        'background-color: white !important;'
        '}'

        'QLabel {'
        'font-size: 11pt;'
        '}'

        'QLineEdit {'
        'font-size: 12pt;'
        '}'

        'QComboBox {'
        'font-size: 12pt;'
        '}'
    )
    # endregion

    # region Sizing
    window_h = {
        "9": 550,
        "16": 850,
    }

    window_w = {
        "9": 800,
        "16": 1200
    }

    grid_side = {
        "9": 450,
        "16": 765
    }

    cell_value_side = 42

    cell_hint_side = 14
    # endregion