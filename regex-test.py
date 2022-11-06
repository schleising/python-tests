import re
from re import Pattern

class Requirements():
    def __init__(self) -> None:
        self._reqs = 'dL16-PRS302-987kjICMST-876s\rbL16-PRS32-765dL16-PRS3.2-432kCMS-GS-971jaCMS-GS-876bCMS-123sCMS-654jL16-PRS3.2-1234keCMS-123bf\tkCMS-2345jb;o\nsaICMST-SSS-1234cjbaCMS-GS-1234s;cjICMST-SSS-9876bsac;jbsdICMST-SSS-146ck;jdsbc'
        self.cmsProject = 'CMS-'
        self.cmsRegEx = re.compile(f'({self.cmsProject}([0-9]+))')
        self.l16Project = 'L16-PRS3.2-'
        self.l16EscapedProject = r'L16-PRS3\.2-'
        self.l16RegEx = re.compile(f'({self.l16EscapedProject}([0-9]+))')
        self.cmsGsProject = 'CMS-GS-'
        self.cmsGsRegEx = re.compile(f'({self.cmsGsProject}([0-9]+))')
        self.icmstProject = 'ICMST-SSS-'
        self.icmstRegEx = re.compile(f'({self.icmstProject}([0-9]+))')

    def _GetReqs(self, regex: Pattern[str]) -> list[str]:
        return [result[0] for result in sorted(set(regex.findall(self._reqs)), key=lambda result: int(result[1]))]

    @property
    def cmsReqs(self) -> list[str]:
        reqList = self._GetReqs(self.cmsRegEx)
        return reqList

    @property
    def l16Reqs(self) -> list[str]:
        return self._GetReqs(self.l16RegEx)

    @property
    def cmsGsReqs(self) -> list[str]:
        return self._GetReqs(self.cmsGsRegEx)

    @property
    def icmstReqs(self) -> list[str]:
        return self._GetReqs(self.icmstRegEx)

    @property
    def reqs(self) -> list[str]:
        return self.cmsReqs + self.l16Reqs + self.cmsGsReqs + self.icmstReqs

reqs = Requirements()

print(f'CMS Reqs   : {reqs.cmsReqs}')
print(f'L16 Reqs   : {reqs.l16Reqs}')
print(f'CMS GS Reqs: {reqs.cmsGsReqs}')
print(f'ICMST Reqs : {reqs.icmstReqs}')
print(f'All Reqs   : {reqs.reqs}')
