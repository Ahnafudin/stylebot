// function addQuickReplies() {
//     const quickReplies = [
//       "Hello", "Help", "Contact", "More Info"
//     ];
  
//     const buttonsHTML = quickReplies.map(reply => 
//       `<button class="quick-reply-btn" onclick="sendQuickReply('${reply}')">${reply}</button>`
//     ).join("");
  
//     const quickRepliesHTML = `<div class="quick-replies">${buttonsHTML}</div>`;
//     msgerChat.insertAdjacentHTML("beforeend", quickRepliesHTML);
//     msgerChat.scrollTop += 500;
// }
  
// function sendQuickReply(reply) {
//     appendMessage(PERSON_NAME, PERSON_IMG, "right", reply);
//     botResponse(reply);
//     document.querySelector('.quick-replies').remove(); // Remove quick replies after selection
// }
  
// addQuickReplies(); // Call this function to add quick replies when chatbot loads

// function showTypingIndicator() {
//     const typingIndicatorHTML = `
//       <div class="msg left-msg" id="typing-indicator">
//         <div class="msg-img" style="background-image: url(${BOT_IMG})"></div>
//         <div class="msg-bubble">
//           <div class="typing-indicator">
//             <span></span>
//             <span></span>
//             <span></span>
//           </div>
//         </div>
//       </div>
//     `;
  
//     msgerChat.insertAdjacentHTML("beforeend", typingIndicatorHTML);
//     msgerChat.scrollTop += 500;
// }
  
// function hideTypingIndicator() {
//     const typingIndicator = document.getElementById("typing-indicator");
//     if (typingIndicator) {
//       typingIndicator.remove();
//     }
// }
  
// function botResponse(rawText) {
//       showTypingIndicator();
  
//       $.get("/get", { msg: rawText }).done(function(data) {
//           hideTypingIndicator();
//           const msgText = data;
//           appendMessage(BOT_NAME, BOT_IMG, "left", msgText);
//       });
// }