# Generated by https://quicktype.io

from typing import Optional, List


class FeedbackEmail:
    subject: str
    addresses: str

    def __init__(self, subject: str, addresses: str) -> None:
        self.subject = subject
        self.addresses = addresses


class FeedbackSlack:
    subject: str
    slack_address: str
    slack_api_key: str

    def __init__(self, subject: str, slack_address: str, slack_api_key: str) -> None:
        self.subject = subject
        self.slack_address = slack_address
        self.slack_api_key = slack_api_key


class GenericSettings:
    monitor_interval: int
    feedback_email: FeedbackEmail
    feedback_slack: FeedbackSlack

    def __init__(self, monitor_interval: int, feedback_email: FeedbackEmail, feedback_slack: FeedbackSlack) -> None:
        self.monitor_interval = monitor_interval
        self.feedback_email = feedback_email
        self.feedback_slack = feedback_slack


class Match:
    type: Optional[str]
    value: Optional[str]

    def __init__(self, type: Optional[str], value: Optional[str]) -> None:
        self.type = type
        self.value = value


class EmailTrigger:
    account: str
    username: str
    pw: str
    matches: List[Match]
    robots: List[str]

    def __init__(self, account: str, username: str, pw: str, matches: List[Match], robots: List[str]) -> None:
        self.account = account
        self.username = username
        self.pw = pw
        self.matches = matches
        self.robots = robots


class FileTrigger:
    path: str
    pattern: str
    keywords: List[str]
    robots: List[str]

    def __init__(self, path: str, pattern: str, keywords: List[str], robots: List[str]) -> None:
        self.path = path
        self.pattern = pattern
        self.keywords = keywords
        self.robots = robots


class ScheduleTrigger:
    name: str
    cron: str
    robots: List[str]

    def __init__(self, name: str, cron: str, robots: List[str]) -> None:
        self.name = name
        self.cron = cron
        self.robots = robots


class Triggers:
    email_triggers: List[EmailTrigger]
    file_triggers: List[FileTrigger]
    schedule_triggers: List[ScheduleTrigger]

    def __init__(self, email_triggers: List[EmailTrigger], file_triggers: List[FileTrigger], schedule_triggers: List[ScheduleTrigger]) -> None:
        self.email_triggers = email_triggers
        self.file_triggers = file_triggers
        self.schedule_triggers = schedule_triggers


class TopLevel:
    triggers: Triggers
    generic_settings: GenericSettings

    def __init__(self, triggers: Triggers, generic_settings: GenericSettings) -> None:
        self.triggers = triggers
        self.generic_settings = generic_settings