function exportToCsv($, Papa) {
    $('#export').on('click', function(e) {
        var tableData = [];
        $('#org-table tbody tr').each(function(rowIndex, r) {
            var cols = [];
            $(this).find('td').each(function(colIndex, c) {
                cols.push(c.textContent);
            });
            tableData.push(cols);
        });

        var csv = Papa.unparse({
            fields: ["№", "Organization Name", "Website", "Contact Information", "Specialization"],
            data: tableData
        });

        var blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
        var link = document.createElement("a");
        link.href = URL.createObjectURL(blob);
        link.style = "visibility:hidden";
        link.download = 'Organization_Data.csv';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    });
}
``
