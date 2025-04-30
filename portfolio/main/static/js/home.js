document.addEventListener('DOMContentLoaded', function() {
    setTimeout(function() {
        const searchInput = document.getElementById('name-search');
        const tags = document.querySelectorAll('.tag');
        const projects = document.querySelectorAll('.project');
        
        if (!searchInput || tags.length === 0 || projects.length === 0) {
            console.error('Один из элементов не найден!');
            return;
        }

        const filterProjects = () => {
            // Получаем активный тег, если он есть
            const activeTagElement = document.querySelector('.tag.active');
            const activeTag = activeTagElement ? activeTagElement.dataset.tag : null;
            const searchTerm = searchInput.value.toLowerCase().trim();
            
            projects.forEach(project => {
                const projectName = project.dataset.name?.toLowerCase() || '';
                const projectTags = project.dataset.tag?.toLowerCase() || '';
                const projectTagsArray = projectTags.split(',').map(t => t.trim());
                
                const nameMatch = projectName.includes(searchTerm);
                // Если тег не выбран (activeTag === null), показываем все по тегам
                const tagMatch = !activeTag || projectTagsArray.includes(activeTag);
                
                project.style.display = (nameMatch && tagMatch) ? 'block' : 'none';
            });
        };

        // Поиск по имени
        searchInput.addEventListener('input', filterProjects);
        
        // Фильтр по тегам с возможностью отмены выбора
        tags.forEach(tag => {
            tag.addEventListener('click', function() {
                if (this.classList.contains('active')) {
                    // Если кликнули по уже активному тегу - снимаем выделение
                    this.classList.remove('active');
                } else {
                    // Снимаем выделение со всех тегов и выделяем текущий
                    tags.forEach(t => t.classList.remove('active'));
                    this.classList.add('active');
                }
                filterProjects();
            });
        });
        
        // Начальная фильтрация без выбранных тегов (показываем все)
        filterProjects();
    }, 100);
});
