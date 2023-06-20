function generateOrganizations($) {
    $('#org-form').on('submit', function(e) {
        e.preventDefault();
        $('#loader').removeClass('hidden');
        var generated_organizations = 0;
        var organization_number = 0;
        var total_organizations = $('#org-number').val();
        var description = $('#description-switch').prop('checked') ? $('#customPrompt').val() : undefined;

        var generate = function() {
            var data = { number_of_organizations: Math.min(10, total_organizations - generated_organizations) };
            if(description !== undefined) {
                data.description = description;
            }
            $.ajax({
                type: "POST",
                url: "/generate",
                data: data,
                success: function(response) {
                    generated_organizations += response.length;
                    response.forEach(function(org) {
                        organization_number++;
                        $('#org-table tbody').append(
                            '<tr>' +
                                '<td>' + organization_number + '</td>' +
                                '<td>' + org['Organization Name'] + '</td>' +
                                '<td><a href="' + org['Website'] + '" target="_blank">' + org['Website'] + '</a></td>' +
                                '<td>' + org['Contact Information'] + '</td>' +
                                '<td>' + org['Specialization'] + '</td>' +
                            '</tr>'
                        );
                    });
                    var tableData = $('#org-table tbody').html();
                    localStorage.setItem('orgData', JSON.stringify(tableData));
                    if (generated_organizations < total_organizations) {
                        generate();
                    } else {
                        $('#loader').addClass('hidden');
                    }
                }
            });
        };

        generate();
    });
}
