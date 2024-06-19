# Google Analytics

## 知识点

`sqs允许公开接收队列的消息`

## 解题

[参考teamssix文章](https://wiki.teamssix.com/CloudService/IAM/the_big_iam_challenge_writeup.html)

题目给出的`Policy`如下

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "sqs:SendMessage",
                "sqs:ReceiveMessage"
            ],
            "Resource": "arn:aws:sqs:us-east-1:092297851374:wiz-tbic-analytics-sqs-queue-ca7a1b2"
        }
    ]
}
```

这个`Policy`授予了所有人拥有这个`SQS`队列的发送、接收消息的权限

SQS (Simple Queue Service) 可以用来帮助不同的应用程序之间进行可靠的消息传递，它就像是一个消息中转站，可以把消息从一个地方发送到另一个地方，确保消息的安全送达和处理，让应用程序之间更好地进行通信和协作。

根据官方文档，要调用 Receive Message 接口，需要知道 Queue URL，Queue URL 的主要构成部分就是 Account ID 和 Queue，在题目的 Policy 中给出了 Account ID 和 Queue 的值，那么我们就可以构造这个 Queue URL 了，构造后的 Queue URL 为：https://queue.amazonaws.com/092297851374/wiz-tbic-analytics-sqs-queue-ca7a1b2

最后，使用 AWS CLI 的 SQS 服务里的 receive-message 接口，利用 --queue-url 参数指定这个队列的 URL 地址。