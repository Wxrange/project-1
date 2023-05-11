import csv
import os.path
import re
from PyQt5.QtWidgets import *
from view_2 import *
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Controller(QMainWindow, Ui_MainWindow):
    """
    The Class Controller contains the details of proccessing and validation of user input
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        Method __init__ checks for input and where the input goes
        :param args: Takes all the arugments from the user input with the GUI
        :param kwargs: Takes all the key argurments from the user input with the GUI
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(lambda: self.confirm_2())
        self.pushButton_3.clicked.connect(lambda: self.confirm_3())

    def main(self, input_file, output_file) -> None:
        """
        Method main processes the input file and sends it to the output file
        :return: None
        """
        list_1: list = []
        # tested
        with open(input_file, 'r', ) as text_file:
            with open(output_file, 'w', newline='') as csv_file:
                content = csv.writer(csv_file)
                content.writerow(['Email', 'Subject', 'Confidence'])
                for line in text_file:
                    if re.search('^From:', line):
                        list_1.append(line.rstrip().split()[1])
                    elif re.search('^Subject:', line):
                        list_1.append(line.rstrip().split()[4])
                    elif re.search('^X-DSPAM-Confidence:', line):
                        list_1.append(line.rstrip().split()[1])
                    if len(list_1) == 3:
                        content.writerow(list_1)
                        list_1.clear()
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit.setText("")
        self.pushButton_3.setEnabled(False)
        self.lineEdit_3.setEnabled(False)
        self.label_3.setEnabled(False)
        self.textBrowser.setText("data stored")

    def confirm_2(self) -> None:
        """
        Method confirm_2 takes the 2 inputs the input, and output file and validates if the user inputed the correct file names
        :return: None
        """
        file_exist_input: bool = True
        file_exist_output: bool = False
        while True:
            input_file: str = self.lineEdit.text().strip()
            try:
                with open('files/'+ input_file,'r') as file:
                    break
            except FileNotFoundError:
                self.textBrowser.setText('File does not exist!')
                file_exist_input = False
                break
        print(f'files/{input_file}')


        output_file: str = self.lineEdit_2.text().strip()
        output_file_converted: str = f"files/{output_file}"
        input_file_converted: str = f"files/{input_file}"
        while os.path.isfile(output_file_converted):
            # Unhide the label and textbox
            file_exist_output = True
            self.textBrowser.setText('Override the existing file (y/n)')
            self.pushButton_3.setEnabled(True)
            self.lineEdit_3.setEnabled(True)
            self.label_3.setEnabled(True)
            break

        if output_file_converted == "files/":
            self.textBrowser.setText('Enter a character(a,1, etc.)')
        elif file_exist_input == True and file_exist_output == False:
            self.main(input_file_converted, output_file_converted)

    def confirm_3(self) -> None:
        """
        Method confirm 3 overrides the existing output file
        :return: None
        """
        # The point is to address that we need a seperate section that the user needs to input if overriding
        output_file: str = self.lineEdit_2.text()
        input_file: str = self.lineEdit.text()
        response: str = self.lineEdit_3.text().strip().lower()
        input_file_converted: str = f"files/{input_file}"
        output_file_converted: str = f"files/{output_file}"
        while os.path.isfile(output_file_converted):
            if response == 'y':
                self.main(input_file_converted, output_file_converted)
            elif response == 'n':
                self.textBrowser.setText('New output file name:')
                self.lineEdit_2.setText("")
            else:
                self.textBrowser.setText('Input (y/n)')
                self.lineEdit_3.setText("")
            break






