from ..schema.nexusphp import Attendance
from ..utils.net_utils import NetUtils


class MainClass(Attendance):
    URL = 'https://lemonhd.org/'
    USER_CLASSES = {
        'downloaded': [2199023255552, 8796093022208],
        'share_ratio': [4, 5.5],
        'days': [175, 364]
    }

    def build_selector(self):
        selector = super(MainClass, self).build_selector()
        NetUtils.dict_merge(selector, {
            'detail_sources': {
                'default': {
                    'elements': {
                        'bar': '#info_block'
                    }
                }
            },
            'details': {
                'seeding': {
                    'regex': '做种数.*?(\\d+)'
                },
                'leeching': {
                    'regex': '下载数.*?(\\d+)'
                }
            }
        })
        return selector
