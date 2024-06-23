import PyQt5.QtWidgets as qtw

class Calculator(qtw.QWidget):
    """ 
    
    Creates a keypad that allows for computation using four basic operations. 
    
    Attributes:
        temp_nums (List): The list that stores the current numbers being entered.
        fin_nums (List): The list the stores the joined numbers when an operator is pressed.
        result_field (QLineEdit): The text field provided by PYQT5. 

    """
    def __init__(self) -> None:
        """
    
        Sets a grid layout for the Calculator and initializes the keypad.
        Initializes the temp_nums and fin_nums list.
        
        """
        super().__init__()
        self.setLayout(qtw.QGridLayout())
        self.create_keypad()
        self.temp_nums = []
        self.fin_nums = []

    def create_keypad(self) -> None:
        """
        
        Adds the appropriate widgets to create a calculator.

        """
        self.result_field = qtw.QLineEdit()
        self.layout().addWidget(self.result_field, 0, 0, 1, 4)
        self.layout().addWidget(qtw.QPushButton('Result (=)', clicked = self.func_result), 1, 0, 1, 2) 
        self.layout().addWidget(qtw.QPushButton('Clear', clicked = self.clear_calc), 1, 2, 1, 2)
        self.layout().addWidget(qtw.QPushButton('9', clicked = lambda : self.num_press('9')), 2, 0)
        self.layout().addWidget(qtw.QPushButton('8', clicked = lambda : self.num_press('8')), 2, 1)  
        self.layout().addWidget(qtw.QPushButton('7', clicked = lambda : self.num_press('7')), 2, 2)  
        self.layout().addWidget(qtw.QPushButton('6', clicked = lambda : self.num_press('6')), 3, 0)
        self.layout().addWidget(qtw.QPushButton('5', clicked = lambda : self.num_press('5')), 3, 1)  
        self.layout().addWidget(qtw.QPushButton('4', clicked = lambda : self.num_press('4')), 3, 2)
        self.layout().addWidget(qtw.QPushButton('3', clicked = lambda : self.num_press('3')), 4, 0)
        self.layout().addWidget(qtw.QPushButton('2', clicked = lambda : self.num_press('2')), 4, 1)  
        self.layout().addWidget(qtw.QPushButton('1', clicked = lambda : self.num_press('1')), 4, 2)
        self.layout().addWidget(qtw.QPushButton('0', clicked = lambda : self.num_press('0')), 5, 0, 1, 3)    
        self.layout().addWidget(qtw.QPushButton('+', clicked = lambda : self.func_press('+')), 2, 3)
        self.layout().addWidget(qtw.QPushButton('-', clicked = lambda : self.func_press('-')), 3, 3)
        self.layout().addWidget(qtw.QPushButton('*', clicked = lambda : self.func_press('*')), 4, 3)
        self.layout().addWidget(qtw.QPushButton('/', clicked = lambda : self.func_press('/')), 5, 3)
    
    def num_press(self, key_num) -> None:
        """
        
        Adds the pressed number to temp_nums and displays the result on the 
        text field. If fin_nums is not empty, we display it first.

        Args:
            key_num: The number that is pressed. 
        
        """
        self.temp_nums.append(key_num)
        temp_str = ''.join(self.temp_nums)
        if self.fin_nums:
            self.result_field.setText(''.join(self.fin_nums) + temp_str)
        else:
            self.result_field.setText(temp_str)

    def func_press(self, operator) -> None: 
        """
        
        Adds the operator to the string of numbers. If the previous character is also
        an operator, then we do not add it to fin_nums.

        Args:
            operator: The operator that is pressed.

        """
        if (len(self.temp_nums) > 0 or len(self.fin_nums) > 0):
            temp_str = ''.join(self.temp_nums)
            self.fin_nums.append(temp_str)
            if ''.join(self.fin_nums)[-1] not in ['+', '-', '*', '/']:
                self.fin_nums.append(operator)
            self.temp_nums = []
            self.result_field.setText(''.join(self.fin_nums))

    def func_result(self) -> None:
        """
        
        Joins the temp_nums and fin_nums to create a string that needs to be
        evaluated. Uses the python eval() function to compute the result and
        display it. 

        """
        self.fin_nums.append(''.join(self.temp_nums))
        result_str = ''.join(self.fin_nums)
        if (len(result_str) != 0):
            result_str = str(eval(result_str))
        self.fin_nums = []
        self.temp_nums = []
        self.fin_nums.append(result_str)
        self.result_field.setText(''.join(self.fin_nums))
    
    def clear_calc(self) -> None:
        """
        
        Clears the result field and also resets the fin_nums and temp_nums list.
        
        """
        self.result_field.clear()
        self.fin_nums = []
        self.temp_nums = []
