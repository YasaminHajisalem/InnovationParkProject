from pulp import LpProblem, LpVariable, LpMaximize, lpSum, LpBinary, value


def solve_lp(startups, total_budget, total_space):

    model = LpProblem("InnovationPark", LpMaximize)

    selected = []

    for i in range(len(startups)):
        selected.append(LpVariable(f"x_{i}", cat=LpBinary))

    # تابع هدف: بیشینه کردن مجموع امتیازها
    model += lpSum(
        startups[i]["score"] * selected[i]
        for i in range(len(startups))
    )

    # محدودیت بودجه
    model += lpSum(
        startups[i]["budget"] * selected[i]
        for i in range(len(startups))
    ) <= total_budget

    # محدودیت فضا
    model += lpSum(
        startups[i]["space"] * selected[i]
        for i in range(len(startups))
    ) <= total_space

    model.solve()

    result = []

    total_score = 0

    for i in range(len(startups)):
        if value(selected[i]) == 1:

            result.append(startups[i])

            total_score += startups[i]["score"]

    return result, total_score