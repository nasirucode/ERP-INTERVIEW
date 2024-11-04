<p>{% if doc.status == 'Draft' %}
    New Timesheet Created
{% else %}
    Timesheet {{ doc.status }}
{% endif %}</p>
