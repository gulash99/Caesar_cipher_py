from typing import Optional

class CaesarsCipher:
    """Класс, реализующий шифр Цезаря для шифрования и расшифровки сообщений."""

    SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."

    def __init__(self) -> None:
        """Инициализация класса CaesarsCipher."""
        self.key: Optional[int] = None

    def encrypt(self, message: str, key: int) -> str:
        """Шифрует сообщение с использованием шифра Цезаря.

        Args:
            Сообщение для шифрования.
            Ключ шифрования.

        Returns:
            Зашифрованное сообщение.
        """
        self.key = key
        return self._shift(message, key)

    def decrypt(self, message: str, key: int) -> str:
        """Расшифровывает сообщение с использованием шифра Цезаря.

        Args:
            Сообщение для расшифровки.
            Ключ для расшифровки.

        Returns:
            Расшифрованное сообщение.
        """
        self.key = key
        return self._shift(message, -key)

    def _shift(self, message: str, key: int) -> str:
        """Сдвигает символы сообщения на заданное количество позиций.

        Args:
            Исходное сообщение.
            Ключ сдвига (положительный или отрицательный).

        Returns:
            Обработанное сообщение (зашифрованное или расшифрованное).
        """
        shifted_message = []
        for symbol in message:
            if symbol in self.SYMBOLS:
                symbol_index = self.SYMBOLS.index(symbol)
                shifted_index = (symbol_index + key) % len(self.SYMBOLS)
                shifted_message.append(self.SYMBOLS[shifted_index])
            else:
                shifted_message.append(symbol)  # Оставляем символы, не входящие
                # в список SYMBOLS, без изменений
        return ''.join(shifted_message)


def find_key_and_decrypt(encrypted_message: str) -> None:
    """Автоматически подбирает ключ для расшифровки сообщения и записывает
    результат в файл.

    Args:
        Зашифрованное сообщение.
        # output_file: Путь к файлу, куда записать расшифрованное сообщение.
    """
    cipher = CaesarsCipher()
    for key in range(len(CaesarsCipher.SYMBOLS)):
        possible_message = cipher.decrypt(encrypted_message, key)
        print(f"{key}: {possible_message}")


if __name__ == '__main__':
    encrypted_message = "o3zR v..D0?yRA0R8FR8v47w0ER4.R1WdC!sLF5D"
    find_key_and_decrypt(encrypted_message)