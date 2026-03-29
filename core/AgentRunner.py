from Agents.syntaxChecker import SyntaxChecker
from Agents.LogicReasoner import LogicReasoner
from Agents.fixSuggestor import FixSuggester


def run_agents(code: str):
    checker = SyntaxChecker()
    reasoner = LogicReasoner()
    suggester = FixSuggester()

    syntax_report = checker.check(code)
    logic = reasoner.reason(code)
    fix = suggester.suggest(syntax_report, logic)

    return fix