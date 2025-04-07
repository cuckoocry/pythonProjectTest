

if __name__ == '__main__':
    send_data = [[
        {
            "sysCode": "system1",
            "sendTitle": "通知",
            "templateId": "template123",
            "templateKeyMap": {"key1": "value1", "key2": "value2"},
            "receiveBy": "user1"
        },
        {
            "sysCode": "system2",
            "sendTitle": "提醒",
            "templateId": "template456",
            "templateKeyMap": {"key1": "value3", "key2": "value4"},
            "receiveBy": "user2"
        }
    ]]
    print(send_data)




