function messageParser(message) {
    var result = "";
    const msgType = ["channel_post", "message"];
    for (var n = 0; n < msgType.length; n++) {
        if (msgType[n] in message) {
            result += messageToHtml(message[msgType[n]]);
        }
    }
    return result;
}

function messageToHtml(message) {
    var result = "";

    try { result += "标识：" + getContent(message, ["chat", "id"]) } catch { }
    try { result += " : " + getContent(message, ["message_id"]) } catch { }
    try { result += "<br> 对话：" + getContent(message, ["chat", "title"]) } catch { }
    try { result += " <= " + getContent(message, ["sender_chat", "title"]) } catch { }
    try { result += "<br> 用户：" + getContent(message, ["from", "first_name"]) } catch { }
    try { result += " @ " + getContent(message, ["from", "username"]) } catch { }
    try { result += "<br> 作者：" + getContent(message, ["author_signature"]) } catch { }
    try { result += "<br> 时间：" + new Date(getContent(message, ["date"]) * 1000).toLocaleString() } catch { }
    try { result += "<br> 内容：" + getContent(message, ["text"]) } catch { }
    try { result += "<br> 内容：" + getContent(message, ["caption"]) } catch { }
    try { result += "<br> 图片：" + getContent(message, ["photo"]).length } catch { }
    try { result += "<br> 视频：" + getContent(message, ["video", "mime_type"]) } catch { }
    try { result += "<br> 文件：" + getContent(message, ["document", "mime_type"]) } catch { }
    try { result += "<br> 贴纸：" + getContent(message, ["sticker", "emoji"]) } catch { }
    try { result += "<br> 投票：" + getContent(message, ["poll", "question"]) } catch { }
    try { result += "<br> 名片：" + getContent(message, ["contact", "first_name"]) + " @ " + getContent(message, ["contact", "phone_number"]) } catch { }
    try { result += "<br> 回复：" + { true: "Yes." }[typeof getContent(message, ["reply_to_message"]) == "object"] } catch { }

    return result;
}

function getContent(content, parameters = []) {
    if (typeof parameters == "object" && parameters.length == 1) parameters = parameters[0];
    if (typeof parameters == "string" && content[parameters]) return content[parameters];
    else return getContent(content[parameters[0]], parameters.pop());
}
