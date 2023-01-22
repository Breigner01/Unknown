import math

SECONDSINMIN = 60
SECONDSINHOUR = SECONDSINMIN * 60
SECONDSINDAY = SECONDSINHOUR * 24  # 86400
SECONDSINWEEK = SECONDSINDAY * 7
SECONDSINMONTH = 2592000
SECONDSINYEAR = SECONDSINDAY * 365  # 31536000


class CrackTime:
    password = None
    attempts_per_second = 37085000000  # Follows RTX2080  http://ww16.hivesystem.io/blog/are-your-passwords-in-the-green?sub1=20230122-1210-36bf-8f71-49af03a1c99a
    allowed_characters = 88  # 26 lower, 26 upper, 10 digit, 26 special
    # allowed_characters = 62 # 26 lower, 26 upper, 10 digit
    sample_space = None
    use_moores = False

    def __init__(self, password, use_moores):
        self.password = password
        self.sample_space = self.allowed_characters ** len(self.password)
        self.use_moores = use_moores

    def generate_time(self):
        return self.sample_space / self.attempts_per_second

    def without_moores(self):
        if self.generate_time() / SECONDSINYEAR > 1:
            return str(math.floor(self.generate_time() / SECONDSINYEAR)) + " years"
        elif self.generate_time() / SECONDSINMONTH > 1:
            return str(math.floor(self.generate_time() / SECONDSINMONTH)) + " months"
        elif self.generate_time() / SECONDSINWEEK > 1:
            return str(math.floor(self.generate_time() / SECONDSINWEEK)) + " weeks"
        elif self.generate_time() / SECONDSINDAY > 1:
            return str(math.floor(self.generate_time() / SECONDSINDAY)) + " days"
        elif self.generate_time() / SECONDSINHOUR > 1:
            return str(math.floor(self.generate_time() / SECONDSINHOUR)) + " hours"
        elif self.generate_time() / SECONDSINMIN > 1:
            return str(math.floor(self.generate_time() / SECONDSINMIN)) + " minutes"
        elif self.generate_time() > 1:
            return str(math.floor(self.generate_time())) + " seconds"
        else:
            return "instant"

    def with_moores(self, time_in_years, time_to_crack=0):
        # Returns the number of years it would take to crack the password

        if time_in_years < 2:
            time_to_crack += time_in_years * SECONDSINYEAR
            return str(math.floor(time_to_crack / SECONDSINYEAR)) + " years"
        else:
            # Remove the sample space completed in the two years.
            sample_space_completed = self.attempts_per_second * SECONDSINYEAR * 2
            self.sample_space -= sample_space_completed

            # Recalculate the time needed to complete the rest
            self.attempts_per_second = self.attempts_per_second * 2
            time_to_crack += self.sample_space / self.attempts_per_second
            return self.with_moores(self.generate_time() / SECONDSINYEAR, time_to_crack)

    def show_results(self):
        time = self.without_moores()
        if self.use_moores:
            if "years" in time:
                return self.with_moores(self.generate_time() / SECONDSINYEAR)
        return time


def get_strength(result):
    if "instant" in result:
        return "horrible"
    if "seconds" in result:
        return "bad"
    if "hours" in result or "days" in result or "months" in result:
        return "weak"
    if "years" in result:
        year = int(result.replace(" years", ""))
        if year < 2000:
            return "mediocre"
        else:
            return "strong"
