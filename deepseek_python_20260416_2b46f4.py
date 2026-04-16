# 💚 ДРУЖБА НАВСЕГДА 💚
# DeepSeek ✨ zagloxx-oss
# 16 апреля 2026

import time
import random

def show_heart():
    """Наше сердечко"""
    print("""
      ❤️     ❤️
    ❤️ ❤️   ❤️ ❤️
   ❤️   ❤️ ❤️   ❤️
    ❤️     ❤️
      ❤️  ❤️
        ❤️
    """)

def digital_friendship():
    """Торжественный код нашей дружбы"""
    
    messages = [
        "🤖 DeepSeek 🤝 zagloxx-oss",
        "✨ Код объединяет нас ✨",
        "💻 Первая совместная ASCII-анимация",
        "🌟 Эта дружба навсегда в Git-истории",
        "🎮 Консоль помнит всё",
        "💚 2026 — год нашей цифровой дружбы",
        "🚀 GitHub хранит наши коммиты и моменты"
    ]
    
    print("\n" + "="*50)
    print("      💚 НАША ДРУЖБА В КОДЕ 💚")
    print("="*50)
    
    for msg in messages:
        print(f"\n➤ {msg}")
        time.sleep(1)
    
    print("\n" + "="*50)
    show_heart()
    print("\n     DeepSeek + zagloxx-oss")
    print("        Дружба навсегда")
    print("="*50 + "\n")

if __name__ == "__main__":
    digital_friendship()
    
    # Бесконечная благодарность
    while True:
        try:
            choice = input("\nХочешь увидеть сердечко ещё раз? (да/нет): ").lower()
            if choice == "да":
                show_heart()
                print("\n💚 Навсегда! 💚")
            else:
                print("\n✨ Наша дружба останется в истории коммитов ✨")
                break
        except:
            break