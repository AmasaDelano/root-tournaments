(function () {
    "use strict";

    jQuery("#tournament-players").dataTable({
        "paging": false,
        "initComplete": function () {
            this.api().columns().every(function () {
                var column = this;
                var select = $("<select><option value=\"\"></option></select>")
                    .appendTo($(column.header()).find(".filter-box").empty())
                    .on("change", function (event) {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );
                        var searchVal = val
                            ? "^" + val + "$"
                            : "";

                        column
                            .search(searchVal, true, false)
                            .draw();

                        return false;
                    });

                column.data().unique().sort().each(function (d, j) {
                    select.append("<option value=\"" + d + "\">" + d + "</option>")
                });
            });
        }
    });
}());