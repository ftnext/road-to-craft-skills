from collections.abc import Iterable


class NewCasesReporter:
    def __init__(self) -> None:
        self.total_cases = 0
        self.state_counts = {}
        self.counties = []

    def make_report(self, county_csv: str) -> str:
        county_lines = county_csv.split("\n")
        self.calculate_counties(county_lines)
        report = (
            ""
            + "County     State     Avg New Cases\n"
            + "======     =====     =============\n"
        )
        for county in self.counties:
            report += f"{county.county: <11}{county.state: <10}{county.rolling_average:.2f}\n"
        report += "\n"
        states = set(self.state_counts.keys())
        for state in sorted(states):
            report += f"{state} cases: {self.state_counts[state]}\n"
        report += f"Total Cases: {self.total_cases}\n"
        return report

    def calculate_counties(self, lines: Iterable[str]) -> None:
        self.total_cases = 0
        self.state_counts.clear()
        self.counties.clear()

        for line in lines:
            tokens = line.split(",")
            county = County()
            county.county = tokens[0].strip()
            county.state = tokens[1].strip()
            # compute rolling average
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
            county.rolling_average = sum_ / n

            # compute sum of cases
            cases = 0
            i = 2
            while i < len(tokens):
                cases += int(tokens[i].strip())
                i += 1
            self.total_cases += cases
            state_count = self.state_counts.get(county.state, 0)
            self.state_counts[county.state] = state_count + cases
            self.counties.append(county)


class County:
    def __init__(self):
        self.county = None
        self.state = None
        self.rolling_average = float("nan")
