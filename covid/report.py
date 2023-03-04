from collections.abc import Iterable


class NewCasesCalculator:
    def __init__(self) -> None:
        self.total_cases = 0
        self.state_counts = {}
        self.counties = []

    def calculate_counties(self, county_lines: Iterable[str]) -> None:
        self.total_cases = 0
        self.state_counts.clear()
        self.counties.clear()

        for county_line in county_lines:
            county = self.calculate_county(county_line)
            self.counties.append(county)

    def calculate_county(self, line: str) -> "County":
        county = County()
        tokens = line.split(",")
        county.county = tokens[0].strip()
        county.state = tokens[1].strip()
        county.rolling_average = self.calculate_rolling_average(tokens)
        cases = self.calculate_sum_of_cases(tokens)
        self.increment_state_counter(county.state, cases)
        return county

    def calculate_rolling_average(self, tokens: list[str]) -> float:
        last_day = len(tokens) - 1
        first_day = last_day - 7 + 1
        if first_day < 2:
            first_day = 2
        n = last_day - first_day + 1
        sum_ = 0
        day = first_day
        while day <= last_day:
            sum_ += int(tokens[day].strip())
            day += 1
        return sum_ / n

    def calculate_sum_of_cases(self, tokens: list[str]) -> int:
        cases = 0
        i = 2
        while i < len(tokens):
            cases += int(tokens[i].strip())
            i += 1
        self.total_cases += cases
        return cases

    def increment_state_counter(self, state: str, cases: int):
        state_count = self.state_counts.get(state, 0)
        self.state_counts[state] = state_count + cases


class NewCasesReporter(NewCasesCalculator):
    def make_report(self, county_csv: str) -> str:
        county_lines = county_csv.split("\n")
        self.calculate_counties(county_lines)
        report = self.make_header()
        report += self.make_county_details()
        report += "\n"
        report += self.make_state_totals()
        report += f"Total Cases: {self.total_cases}\n"
        return report

    def make_header(self) -> str:
        return (
            ""
            + "County     State     Avg New Cases\n"
            + "======     =====     =============\n"
        )

    def make_county_details(self) -> str:
        county_details = ""
        for county in self.counties:
            county_details += f"{county.county: <11}{county.state: <10}{county.rolling_average:.2f}\n"
        return county_details

    def make_state_totals(self) -> str:
        state_totals = ""
        states = set(self.state_counts.keys())
        for state in sorted(states):
            state_totals += f"{state} cases: {self.state_counts[state]}\n"
        return state_totals


class County:
    def __init__(self):
        self.county = None
        self.state = None
        self.rolling_average = float("nan")
