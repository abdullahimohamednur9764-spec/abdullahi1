class WasteService:
    def __init__(self, name, rate_per_kg):
        self.name = name
        self.rate = rate_per_kg

    def calculate_cost(self, kgs):
        return kgs * self.rate


class Recycling(WasteService):
    def calculate_cost(self, kgs):
        return (kgs * self.rate) * 0.5   # 50% discount


class Hazardous(WasteService):
    def calculate_cost(self, kgs):
        return (kgs * self.rate) + 1000  # extra handling fee


class WasteApp:
    def __init__(self):
        self.jobs = []
        self.job_id = 1
        self.services = {
            "1": WasteService("General Garbage", 50),
            "2": Recycling("Plastic / Paper", 50),
            "3": Hazardous("Medical / Chemical", 150)
        }

    def menu(self):
        while True:
            print("\n--- SMART WASTE MANAGER ---")
            print("1. New Collection Job")
            print("2. View All Jobs")
            print("3. Search Job")
            print("4. Update Weight")
            print("5. Calculate Bill & Pay")
            print("6. Exit")

            choice = input("Select Option: ")

            if choice == "1":
                self.add_job()
            elif choice == "2":
                self.view_jobs()
            elif choice == "3":
                self.search_job()
            elif choice == "4":
                self.update_job()
            elif choice == "5":
                self.pay_bill()
            elif choice == "6":
                print("Exiting system.")
                break
            else:
                print("Invalid choice.")

    def add_job(self):
        client = input("Client Name: ")
        location = input("Location: ")

        print("\nSelect Waste Type:")
        for key, service in self.services.items():
            print(f"{key}. {service.name}")

        s_choice = input("Choice: ")

        if s_choice not in self.services:
            print("Invalid waste type.")
            return

        job = {
            "id": self.job_id,
            "client": client,
            "location": location,
            "service": self.services[s_choice],
            "kgs": 0,
            "paid": False
        }

        self.jobs.append(job)
        self.job_id += 1
        print("Job added successfully.")

    def view_jobs(self):
        if not self.jobs:
            print("No jobs available.")
            return

        print("\n--- ACTIVE JOBS ---")
        for job in self.jobs:
            status = "PAID" if job["paid"] else "UNPAID"
            print(
                f"ID: {job['id']} | Client: {job['client']} | "
                f"Location: {job['location']} | "
                f"Type: {job['service'].name} | "
                f"KGs: {job['kgs']} | Status: {status}"
            )

    def search_job(self):
        jid = input("Enter Job ID: ")
        for job in self.jobs:
            if str(job["id"]) == jid:
                print(job)
                return
        print("Job not found.")

    def update_job(self):
        jid = input("Enter Job ID: ")
        for job in self.jobs:
            if str(job["id"]) == jid:
                try:
                    job["kgs"] = float(input("Enter weight (KGs): "))
                    print("Weight updated.")
                except ValueError:
                    print("Invalid number.")
                return
        print("Job not found.")

    def pay_bill(self):
        jid = input("Enter Job ID to pay: ")

        for job in self.jobs:
            if str(job["id"]) == jid:
                if job["kgs"] <= 0:
                    print("Weight not recorded.")
                    return

                total = job["service"].calculate_cost(job["kgs"])
                print("\n--- BILL ---")
                print(f"Client: {job['client']}")
                print(f"Waste Type: {job['service'].name}")
                print(f"Weight: {job['kgs']} KGs")
                print(f"Total Amount: KES {total}")

                print("Payment Method: 1. Mpesa  2. Cash")
                input("Confirm payment...")

                job["paid"] = True
                print("Payment successful.")
                return

        print("Job not found.")


if __name__ == "__main__":
    app = WasteApp()
    app.menu()