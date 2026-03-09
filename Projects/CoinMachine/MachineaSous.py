import sys
import random
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
    QMessageBox, QHBoxLayout
)
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt

# === Paramètres du jeu ===
symbols = ["🍒", "🍋", "🔔", "💎", "🍀", "7️⃣"]
weights = [30, 25, 20, 15, 8, 2]
initial_balance = 100
goal_amount = 500

custom_gains = {
    "🍒": {"3": 4, "2": 1.5},
    "🍋": {"3": 3, "2": 1.3},
    "🔔": {"3": 6, "2": 2},
    "💎": {"3": 8, "2": 3},
    "🍀": {"3": 10, "2": 4},
    "7️⃣": {"3": 15, "2": 5, "1": 1.5}
}

class SlotMachine(QWidget):
    def __init__(self):
        super().__init__()
        self.balance = initial_balance
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Machine à sous 🎰")
        self.setFixedSize(400, 420)

        layout = QVBoxLayout()

        self.label_title = QLabel("🎰 Machine à sous")
        self.label_title.setFont(QFont("Arial", 20))
        self.label_title.setAlignment(Qt.AlignCenter)

        self.label_balance = QLabel(f"💰 Solde : {self.balance}€")
        self.label_balance.setFont(QFont("Arial", 14))
        self.label_balance.setAlignment(Qt.AlignCenter)

        self.label_slots = QLabel("🎲 🎲 🎲")
        self.label_slots.setFont(QFont("Arial", 40))
        self.label_slots.setAlignment(Qt.AlignCenter)

        self.entry_bet = QLineEdit("10")
        self.entry_bet.setFont(QFont("Arial", 14))
        self.entry_bet.setAlignment(Qt.AlignCenter)

        self.btn_spin = QPushButton("Lancer")
        self.btn_spin.setFont(QFont("Arial", 14))
        self.btn_spin.clicked.connect(self.play)

        self.btn_rules = QPushButton("Règles")
        self.btn_rules.setFont(QFont("Arial", 10))
        self.btn_rules.clicked.connect(self.show_rules)

        self.label_message = QLabel("")
        self.label_message.setFont(QFont("Arial", 14))
        self.label_message.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.label_title)
        layout.addWidget(self.label_balance)
        layout.addWidget(self.label_slots)
        layout.addWidget(self.entry_bet)
        layout.addWidget(self.btn_spin)
        layout.addWidget(self.btn_rules)
        layout.addWidget(self.label_message)

        self.setLayout(layout)

    def show_rules(self):
        rules = (
            "🎰 RÈGLES DU JEU 🎰\n\n"
            "🎯 Objectif : Atteindre 500€ pour gagner.\n"
            "💼 Solde initial : 100€\n\n"
            "🔢 À chaque tour : entrez une mise et cliquez sur Lancer.\n\n"
            "💥 Gains selon les symboles :\n"
            "🍒 → x4 (3x), x1.5 (2x)\n"
            "🍋 → x3 (3x), x1.3 (2x)\n"
            "🔔 → x6 (3x), x2 (2x)\n"
            "💎 → x8 (3x), x3 (2x)\n"
            "🍀 → x10 (3x), x4 (2x)\n"
            "7️⃣ → x15 (3x), x5 (2x), x1.5 (1x)\n\n"
            "🎲 Bonne chance et amuse-toi bien !"
        )
        QMessageBox.information(self, "Règles du jeu", rules)

    def spin_slots(self):
        return random.choices(symbols, weights=weights, k=3)

    def calculate_payout(self, result, bet):
        counts = {s: result.count(s) for s in set(result)}
        best_payout = 0
        best_message = "😢 Aucun gain."
        best_color = "red"

        for symbol, count in counts.items():
            gains = custom_gains.get(symbol, {})
            if count == 3 and "3" in gains:
                m = gains["3"]
                payout = bet * m
                if payout > best_payout:
                    best_payout = payout
                    best_message = f" x{m}\nGain : {int(payout)}€"
                    best_color = self.get_color(m)
            elif count == 2 and "2" in gains:
                m = gains["2"]
                payout = int(bet * m)
                if payout > best_payout:
                    best_payout = payout
                    best_message = f" x{m}\nGain : {payout}€"
                    best_color = self.get_color(m)
            elif count == 1 and symbol == "7️⃣" and "1" in gains:
                m = gains["1"]
                payout = int(bet * m)
                if payout > best_payout:
                    best_payout = payout
                    best_message = f" x{m}\nGain : {payout}€"
                    best_color = self.get_color(m)

        return best_payout, best_message, best_color

    def get_color(self, multiplier):
        if multiplier >= 10:
            return "gold"
        elif multiplier >= 5:
            return "orange"
        elif multiplier >= 2:
            return "blue"
        else:
            return "green"

    def play(self):
        try:
            bet = int(self.entry_bet.text())
            if bet <= 0 or bet > self.balance:
                raise ValueError
        except ValueError:
            QMessageBox.critical(self, "Erreur", "Mise invalide ou supérieure au solde.")
            return

        self.balance -= bet
        result = self.spin_slots()
        payout, message, color = self.calculate_payout(result, bet)
        self.balance += payout

        self.label_slots.setText(" | ".join(result))
        self.label_balance.setText(f"💰 Solde : {self.balance}€")
        self.label_message.setText(message)
        self.label_message.setStyleSheet(f"color: {color};")

        if self.balance == 0:
            QMessageBox.information(self, "Perdu", "Vous avez tout perdu !")
            self.btn_spin.setEnabled(False)
        elif self.balance >= goal_amount:
            QMessageBox.information(self, "Gagné", f"Félicitations ! Vous avez atteint {self.balance}€ !")
            self.btn_spin.setEnabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    machine = SlotMachine()
    machine.show()
    sys.exit(app.exec_())
