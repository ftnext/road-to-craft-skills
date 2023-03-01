class NewCasesReporter:
    def make_report(self, county_csv: str) -> str:
        total_cases = 0
        state_counts = {}
        counties = []

        lines = county_csv.split("\n")
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
            total_cases += cases
            state_count = state_counts.get(county.state, 0)
            state_counts[county.state] = state_count + cases
            counties.append(county)

        report = (
            ""
            + "County     State     Avg New Cases\n"
            + "======     =====     =============\n"
        )
        for county in counties:
            report += f"{county.county: <11}{county.state: <10}{county.rolling_average:.2f}\n"
        report += "\n"
        states = set(state_counts.keys())
        for state in sorted(states):
            report += f"{state} cases: {state_counts[state]}\n"
        report += f"Total Cases: {total_cases}\n"
        return report


class County:
    def __init__(self):
        self.county = None
        self.state = None
        self.rolling_average = float("nan")
