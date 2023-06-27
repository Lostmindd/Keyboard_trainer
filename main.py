import sys
import KeyboardTrainer

if __name__ == '__main__':
    app = KeyboardTrainer.QApplication(sys.argv)
    app.setStyle("Windows")
    window = KeyboardTrainer.keyboard_trainer()
    window.show()
    sys.exit(app.exec())
