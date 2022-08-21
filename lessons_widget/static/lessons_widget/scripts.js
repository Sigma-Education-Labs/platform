const initLessonsWidget = (event) => {
    var editor = ace.edit("editor");
    editor.session.setMode("ace/mode/javascript");
    editor.setOption("wrap", 35);

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

        if (typeof editor != 'undefined') {
            const codeSnippet = new Function(editor.getValue());
            codeSnippet();
        }
    });
}

window.addEventListener('DOMContentLoaded', initLessonsWidget);

