import random

def solve_ga(company_count, equipment_count):

    companies = []

    for i in range(company_count):
        companies.append(f"شرکت {i+1}")

    equipments = []

    for i in range(equipment_count):
        equipments.append(f"تجهیز {i+1}")

    schedule = []

    for company in companies:

        equipment = random.choice(equipments)

        hour = random.randint(8, 16)

        schedule.append({
            "شرکت": company,
            "تجهیز": equipment,
            "ساعت استفاده": f"{hour}:00"
        })

    score = random.randint(80, 100)

    return schedule, score