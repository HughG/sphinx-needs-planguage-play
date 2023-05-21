Auto-Import
====

.. toctree::

   auto_import_send_data

Note that some of the requirements for Auto-Import apply to :need:`EG` in general, so I have tried to apply qualifier :need:`EG_Config_AutoImport` where necessary to make the distinction, be it to an entire requirement or to parts of it.

.. fr:: Auto-Import
    :id: EG_AutoImport
    :qualifiers: EG_Config_AutoImport
    :priority: :need:`EG_Milestone_AutoImport_MVP`

    It must be possible to configure :need:`EG` to operate in such a way that it does not require data to be manually imported before use.

Milestones
----

.. milestone:: Auto-Import MVP
    :id: EG_Milestone_AutoImport_MVP

    Minimum Viable Product for the :need:`EG_AutoImport` set of features.

.. needtable:: Requirements for this milestone.
    :columns: type_prefix as "Type";id;title
    :colwidths: 10,20,80

    results = [need for need in needs if '`EG_Milestone_AutoImport_MVP`' in need['priority']]
