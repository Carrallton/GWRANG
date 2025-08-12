import psutil
import time
import os
from datetime import datetime
from pathlib import Path

class NetGuardFZ152:
    def __init__(self):
        """Инициализация с соблюдением ФЗ-152"""
        # Все данные хранятся локально
        self.local_storage = True
        self.internet_transmission = False
        
        # Показываем согласие при запуске
        self.show_consent()
    
    def show_consent(self):
        """Показать уведомление о конфиденциальности"""
        self.clear_screen()
        print("=" * 60)
        print("GWRANG - Монитор сетевой активности")
        print("=" * 60)
        print("🛡 СОБЛЮДЕНИЕ ФЗ-152:")
        print("• НЕ собираем персональные данные")
        print("• НЕ передаем данные в интернет")
        print("• Все данные остаются на вашем компьютере")
        print("• Локальный анализ сетевой активности")
        print("=" * 60)
        print()
        input("Нажмите Enter для продолжения...")
    
    def clear_screen(self):
        """Очистить экран"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def format_bytes(self, bytes_value):
        """Форматировать байты в читаемый вид"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if bytes_value < 1024.0:
                return f"{bytes_value:.1f} {unit}"
            bytes_value /= 1024.0
        return f"{bytes_value:.1f} TB"
    
    def show_network_stats(self):
        """Показать базовую сетевую статистику"""
        stats = psutil.net_io_counters()
        print("📊 Сетевая статистика:")
        print(f"   📤 Отправлено: {self.format_bytes(stats.bytes_sent)}")
        print(f"   📥 Получено: {self.format_bytes(stats.bytes_recv)}")
        print(f"   📦 Пакетов отправлено: {stats.packets_sent}")
        print(f"   📦 Пакетов получено: {stats.packets_recv}")
        print()
    
    def show_active_connections(self):
        """Показать активные сетевые соединения"""
        print("🔌 Активные соединения:")
        try:
            connections = psutil.net_connections(kind='inet')
            if not connections:
                print("   Нет активных соединений")
                return
            
            # Показываем первые 10 соединений
            for i, conn in enumerate(connections[:10]):
                if conn.pid is not None:
                    try:
                        process = psutil.Process(conn.pid)
                        process_name = process.name()
                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        process_name = "Unknown"
                    
                    local_addr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
                    remote_addr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
                    
                    print(f"   {i+1:2d}. {process_name[:15]:<15} {local_addr} → {remote_addr}")
                
            if len(connections) > 10:
                print(f"   ... и еще {len(connections) - 10} соединений")
                
        except Exception as e:
            print(f"   Ошибка получения соединений: {e}")
        print()
    
    def run_basic_monitor(self):
        """Запустить базовый мониторинг"""
        self.clear_screen()
        print("GWRANG - Базовый мониторинг")
        print("=" * 40)
        print("🔒 Данные НЕ передаются в интернет")
        print()
        
        self.show_network_stats()
        self.show_active_connections()
        print("🔄 Обновите вручную для новых данных")
        print()
        input("Нажмите Enter для возврата в меню...")
    
    def run_realtime_monitor(self):
        """Запустить мониторинг в реальном времени"""
        self.clear_screen()
        print("GWRANG - Мониторинг в реальном времени")
        print("=" * 50)
        print("🔒 Соответствует ФЗ-152 - данные НЕ передаются")
        print("Нажмите Ctrl+C для остановки")
        print()
        
        try:
            old_stats = psutil.net_io_counters()
            while True:
                time.sleep(1)
                new_stats = psutil.net_io_counters()
                
                # Считаем скорость
                bytes_sent_per_sec = new_stats.bytes_sent - old_stats.bytes_sent
                bytes_recv_per_sec = new_stats.bytes_recv - old_stats.bytes_recv
                
                # Обновляем экран
                self.clear_screen()
                print("GWRANG - Мониторинг в реальном времени")
                print("=" * 50)
                print("🔒 Соответствует ФЗ-152")
                print()
                print("📊 Скорость сети:")
                print(f"   📤 Исходящая: {self.format_bytes(bytes_sent_per_sec)}/с")
                print(f"   📥 Входящая: {self.format_bytes(bytes_recv_per_sec)}/с")
                print()
                print("🔄 Обновляется каждую секунду...")
                print("Нажмите Ctrl+C для остановки")
                
                old_stats = new_stats
                
        except KeyboardInterrupt:
            print("\n\n👋 Мониторинг остановлен")
            input("Нажмите Enter для возврата в меню...")
    
    def show_menu(self):
        """Показать главное меню"""
        self.clear_screen()
        print("GWRANG - Главное меню")
        print("=" * 40)
        print("🔒 Соответствует ФЗ-152")
        print()
        print("1. Базовый мониторинг")
        print("2. Мониторинг в реальном времени")
        print("3. Показать политику конфиденциальности")
        print("0. Выход")
        print()
    
    def show_privacy_policy(self):
        """Показать политику конфиденциальности"""
        self.clear_screen()
        print("ПОЛИТИКА КОНФИДЕНЦИАЛЬНОСТИ GWRANG")
        print("=" * 50)
        print()
        print("1. СОБЛЮДЕНИЕ ФЗ-152")
        print("   - Продукт полностью соответствует Федеральному закону №152-ФЗ")
        print("   - Не собирает персональные данные пользователей")
        print("   - Не передает данные в интернет без согласия")
        print("   - Все данные обрабатываются локально")
        print()
        print("2. СОБИРАЕМЫЕ ДАННЫЕ")
        print("   - Только техническая информация о сетевых соединениях")
        print("   - Данные сохраняются исключительно локально")
        print("   - Нет идентификации пользователей")
        print()
        print("3. ИСПОЛЬЗОВАНИЕ ДАННЫХ")
        print("   - Анализ только для целей сетевой безопасности")
        print("   - Данные не передаются третьим лицам")
        print("   - Пользователь может удалить все данные в любой момент")
        print()
        input("Нажмите Enter для возврата в меню...")
    
    def run(self):
        """Запустить основной цикл программы"""
        while True:
            self.show_menu()
            try:
                choice = input("Выберите действие (0-3): ").strip()
                
                if choice == "1":
                    self.run_basic_monitor()
                elif choice == "2":
                    self.run_realtime_monitor()
                elif choice == "3":
                    self.show_privacy_policy()
                elif choice == "0":
                    print("👋 Спасибо за использование GWRANG!")
                    break
                else:
                    print("❌ Неверный выбор. Попробуйте снова.")
                    time.sleep(2)
                    
            except KeyboardInterrupt:
                print("\n\n👋 Программа завершена пользователем")
                break
            except Exception as e:
                print(f"❌ Ошибка: {e}")
                time.sleep(2)

if __name__ == "__main__":
    app = NetGuardFZ152()
    app.run()