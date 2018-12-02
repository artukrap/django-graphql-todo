# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['GraphQLTests::test_all_issues 1'] = {
    'data': {
        'issues': {
            'edges': [
                {
                    'node': {
                        'commentSet': {
                            'edges': [
                                {
                                    'node': {
                                        'id': 'Q29tbWVudE5vZGU6MQ==',
                                        'message': 'My random message'
                                    }
                                }
                            ]
                        },
                        'id': 'SXNzdWVOb2RlOjE=',
                        'title': 'Test issue'
                    }
                }
            ]
        }
    }
}

snapshots['GraphQLTests::test_issue_query 1'] = {
    'data': {
        'issue': {
            'commentSet': {
                'edges': [
                    {
                        'node': {
                            'id': 'Q29tbWVudE5vZGU6MQ==',
                            'message': 'My random message'
                        }
                    }
                ]
            },
            'id': 'SXNzdWVOb2RlOjE=',
            'title': 'Test issue'
        }
    }
}
