// 等待DOM加载完成
document.addEventListener('DOMContentLoaded', function() {
    // 初始化导航菜单
    initNavigation();
});

function initNavigation() {
    // 获取当前页面路径
    const currentPath = window.location.pathname;
    
    // 高亮当前页面的导航项
    document.querySelectorAll('.nav-menu a').forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
} 