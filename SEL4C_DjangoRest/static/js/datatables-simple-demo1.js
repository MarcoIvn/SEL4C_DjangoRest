window.addEventListener('DOMContentLoaded', event => {
    // Simple-DataTables
    // https://github.com/fiduswriter/Simple-DataTables/wiki

    const tables = document.querySelectorAll(".datatablesSimple");
    
    tables.forEach(function (table) {
        new simpleDatatables.DataTable(table);
    });
});
