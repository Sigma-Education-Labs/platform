const initLessonsWidget = (event) => {
    const lessons = document.querySelectorAll('.sigma-lesson');
    lessons.forEach((lesson) => {
        const title = lesson.children[0];
        const content = lesson.children[1];

        title.addEventListener('click', () => { 
            document.querySelectorAll('.sigma-lesson-content').forEach(e => e.style.display = 'none');
            content.style.display = 'inline';
        });
    });

    const submitButton = document.querySelector('.sigma-code-submit-button');
    submitButton.addEventListener('click', (event) => {
        event.preventDefault();
    });
}

window.addEventListener('DOMContentLoaded', initLessonsWidget);

