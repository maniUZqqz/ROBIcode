function toggleBox(boxNumber) {
    var box = document.getElementById('box' + boxNumber);
    var expandedHeight = 285;
    var collapsedHeight = 95;
    var isExpanded = box.classList.contains('expanded');
    var newHeight = isExpanded ? collapsedHeight : expandedHeight;
    var heightDifference = newHeight - box.offsetHeight;

    box.classList.toggle('expanded');

    for (var i = boxNumber + 1; i <= 6; i++) {
        var nextBox = document.getElementById('box' + i);
        var currentTop = parseInt(nextBox.style.top);
        nextBox.style.top = (currentTop + heightDifference) + 'px';
    }
}