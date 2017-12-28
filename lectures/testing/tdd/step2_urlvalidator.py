import validators
import requests


class URLValidator:

    def validate_url(self, url: str) -> bool:
        syntactically_well_formed = validators.url(url)

        if not syntactically_well_formed:
            raise ValueError("Must supply well formed URL")

        r = requests.get(url)
        # We will only consider OK as valid. 204 is 'invalid' from our perspective
        print(r.text)
        if r.status_code == 200 and len(r.text) > 0:
            return True
        else:
            return False
