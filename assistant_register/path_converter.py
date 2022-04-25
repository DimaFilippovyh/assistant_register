from datetime import datetime, date


class DateConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'
    format = '%Y-%m-%d'

    def to_python(self, value: str):
        return datetime.strptime(value, self.format).date()

    def to_url(self, value: date):
        return value.strftime(self.format)
