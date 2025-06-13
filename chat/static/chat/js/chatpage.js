// Filter friends in sidebar search
document.getElementById('searchInput').addEventListener('input', function () {
  const filter = this.value.toLowerCase();
  const friendItems = document.querySelectorAll('.friend-item');

  friendItems.forEach(item => {
    const name = item.querySelector('.friend-name').textContent.toLowerCase();
    if (name.includes(filter)) {
      item.style.display = '';
    } else {
      item.style.display = 'none';
    }
  });
});

// Add a new message dynamically to the chat list with timestamp
function addMessage(messageText, sentByMe = true) {
  const messageList = document.getElementById('messageList');

  // Create message container div
  const messageDiv = document.createElement('div');
  messageDiv.classList.add('message');
  messageDiv.classList.add(sentByMe ? 'sent' : 'received');

  // Create message text paragraph
  const messageParagraph = document.createElement('p');
  messageParagraph.classList.add('message-text');
  messageParagraph.textContent = messageText;
  messageDiv.appendChild(messageParagraph);

  // Create time element
  const timeSpan = document.createElement('span');
  timeSpan.classList.add('message-time');

  // Format the current time as HH:MM AM/PM
  const now = new Date();
  const hours = now.getHours() % 12 || 12; // convert 0 to 12 for AM/PM format
  const minutes = now.getMinutes().toString().padStart(2, '0');
  const ampm = now.getHours() >= 12 ? 'PM' : 'AM';
  timeSpan.textContent = `${hours}:${minutes} ${ampm}`;

  messageDiv.appendChild(timeSpan);

  messageList.appendChild(messageDiv);
  messageList.scrollTop = messageList.scrollHeight;
}

// Handle sending message on form submit
document.getElementById('messageForm').addEventListener('submit', function (event) {
  event.preventDefault();
  const input = document.getElementById('messageInput');
  const message = input.value.trim();

  if (message) {
    addMessage(message, true);

    // Clear input after sending
    input.value = '';

    // TODO: send message to backend or friend
  }
});

// Function to simulate loading chat with friend clicked
function startChat(friendName, friendInitials) {
  // Update header friend info
  const friendNameElem = document.getElementById('chatFriendName');
  const friendStatusElem = document.getElementById('chatFriendStatus');
  const friendAvatarElem = document.getElementById('chatFriendAvatar');

  friendNameElem.textContent = friendName;
  friendStatusElem.textContent = 'Online';
  friendAvatarElem.textContent = friendInitials;

  // Clear previous messages
  const messageList = document.getElementById('messageList');
  messageList.innerHTML = '';

  // Optionally, load chat messages from server for that friend
}

// Attach click handlers to friend list items dynamically
document.querySelectorAll('.friend-item').forEach(item => {
  item.addEventListener('click', () => {
    const name = item.querySelector('.friend-name').textContent;
    const avatar = item.querySelector('.friend-avatar').textContent;
    startChat(name, avatar);
  });
});
