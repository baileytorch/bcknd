$(document).ready(function () {
    $('#tabla_paises').DataTable({
        "paging": true,
        "ordering": true,
        "searching": true,
        "pageLength": 10
    });
});