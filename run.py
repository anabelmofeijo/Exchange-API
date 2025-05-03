import threading
from app import app
from app.tasks.bai_schedule import run_bai_task
from app.tasks.bic_schedule import run_bic_task
from app.tasks.standard_schedule import run_standard_task

class Run: 
    def bai_database(self):
        run_bai_task()

    def bic_database(self):
        run_bic_task()

    def std_database(self):
        run_standard_task()

    def run_app(self):
        app.run(debug=True, use_reloader=False, host="0.0.0.0", port=5000)

    def main(self):
        thread_app = threading.Thread(target=self.run_app)
        thread1 = threading.Thread(target=self.bai_database)
        thread2 = threading.Thread(target=self.bic_database)
        thread3 = threading.Thread(target=self.std_database)

        thread_app.start()
        thread1.start()
        thread2.start()
        thread3.start()

        thread_app.join()
        thread1.join()
        thread2.join()
        thread3.join()

if __name__ == '__main__':
    try:
        run = Run()
        run.main()
    except Exception as e:
        print(f'Error: {e}')
