import math

SECONDSINMIN = 60
SECONDSINHOUR = SECONDSINMIN * 60
SECONDSINDAY = SECONDSINHOUR * 24 # 86400
SECONDSINWEEK = 604800
SECONDSINMONTH = 2592000
SECONDSINYEAR = SECONDSINDAY * 365 # 31536000

class CrackTime:
    password = None
    attempts_per_second = 37085000000   # Follows RTX2080  http://ww16.hivesystem.io/blog/are-your-passwords-in-the-green?sub1=20230122-1210-36bf-8f71-49af03a1c99a
    # allowed_characters = 88  # 26 lower, 26 upper, 10 digit, 26 special
    allowed_characters = 62
    sample_space = None

    def __init__(self, password):
        self.password = password
        self.sample_space = self.allowed_characters ** len(self.password)
        print("Sample space = ", self.sample_space)

    def generate_time(self):
        return self.sample_space / self.attempts_per_second

    def return_whole(self):
        if pw.generate_time() / SECONDSINYEAR > 1:
            return str(math.floor(pw.generate_time() / SECONDSINYEAR)) + " years"
        elif pw.generate_time() / SECONDSINMONTH > 1:
            return str(math.floor(pw.generate_time() / SECONDSINMONTH)) + " months"
        elif pw.generate_time() / SECONDSINWEEK > 1:
            return str(math.floor(pw.generate_time() / SECONDSINWEEK)) + " weeks"
        elif pw.generate_time() / SECONDSINDAY > 1:
            return str(math.floor(pw.generate_time() / SECONDSINDAY)) + " days"
        elif pw.generate_time() / SECONDSINHOUR > 1:
            return str(math.floor(pw.generate_time() / SECONDSINHOUR)) + " hours"
        elif pw.generate_time() / SECONDSINMIN > 1:
            return str(math.floor(pw.generate_time() / SECONDSINMIN)) + " minutes"
        elif pw.generate_time() > 1:
            return str(math.floor(pw.generate_time())) + " seconds"
        else:
            return "instant"

    def with_moores(self, time_in_years, time_to_crack=0):
        # Returns the number of seconds it would take to crack the password

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


pw = CrackTime("Alexander101")
time = pw.return_whole()
print(time)
if "years" in time:
    print(pw.with_moores(pw.generate_time() / SECONDSINYEAR))
