SECONDSINMIN = 60
SECONDSINHOUR = SECONDSINMIN * 60
SECONDSINDAY = SECONDSINHOUR * 24 # 86400
SECONDSINYEAR = SECONDSINDAY * 365 # 31536000

class CrackTime:
    password = None
    attempts_per_second = 100000
    allowed_characters = 95  # 26 lower, 26 upper, 10 digit, 33 special
    sample_space = None
    time_to_crack = 0

    def __init__(self, password, allowed_characters=95, attempts_per_second=100000, max_length=150):
        self.password = password
        self.attempts_per_second = attempts_per_second
        self.allowed_characters = allowed_characters
        self.sample_space = self.allowed_characters ** len(self.password)

    def recursive(self, time_in_years):
        # Returns the number of seconds it would take to crack the password
        print(time_in_years)
        if time_in_years < 2:
            self.time_to_crack += time_in_years * SECONDSINYEAR
            return self.time_to_crack
        else:
            # Remove the sample space completed in the two years.
            sample_space_completed = self.attempts_per_second * SECONDSINYEAR * 2
            self.sample_space -= sample_space_completed

            # Recalculate the time needed to complete the rest
            self.attempts_per_second = self.attempts_per_second * 2
            self.time_to_crack += self.sample_space / self.attempts_per_second
            self.recursive(self.generate_time() / SECONDSINYEAR)


    def generate_time(self):
        return self.sample_space / self.attempts_per_second




pw = CrackTime("1234567")
# print(pw.sample_space)
# print(pw.generate_time(), "seconds")
# print(pw.generate_time() / SECONDSINMIN, "minutes")
# print(pw.generate_time() / SECONDSINHOUR, "hours")
# print(pw.generate_time() / SECONDSINDAY, "days")
# print(pw.generate_time() / SECONDSINYEAR, "years")
pw.recursive(pw.generate_time() / SECONDSINYEAR)
# print(pw.time_to_crack / SECONDSINYEAR)

print(pw.time_to_crack / SECONDSINYEAR)
