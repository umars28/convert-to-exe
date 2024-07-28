import webview
from screeninfo import get_monitors

def on_loaded(window):
    current_url = window.get_current_url()
    print(f"Current URL: {current_url}")

    if current_url == "https://inventory.personaltesting.my.id/":
        new_url = "https://inventory.personaltesting.my.id/cashier/login"
        print(f"Redirecting to: {new_url}")
        window.load_url(new_url)

def main():
    monitor = get_monitors()[0]
    screen_width = monitor.width
    screen_height = monitor.height

    window = webview.create_window('Kasir', 'https://inventory.personaltesting.my.id/cashier/login', width=screen_width, height=screen_height, x=0, y=0, resizable=True)
    
    window.events.loaded += on_loaded
    
    webview.start()

if __name__ == '__main__':
    main()
