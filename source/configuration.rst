System Configuration
====

Configuration Functions
----

TODO

Configuration Options
----

This section lists some high-level configuration options for :need:`EG`.

Note: These are represented as :term:`Planguage` Qualifiers because certain other requirements may only apply when an option is configured in a certain way.

.. qual:: Auto-Export of generated data.
    :id: EG_Config_Export_Auto
    :rationale: Streamlines workflow.

    When enabled, this option ensures that all :term:`generated data` is exported from the system automatically.  This means the user doesn't need to take any action but it also means they don't have any choice.


.. qual:: Auto-Import of data from an external source.
    :id: EG_Config_AutoImport
    :rationale: See :need:`EG_AutoImport`.
    :priority: :need:`EG_Milestone_AutoImport_MVP`

    When enabled, :need:`EG_AutoImport` and all its sub-functions and related requirements are applicable.  Enabling this option implies :need:`EG_Config_Export_Auto` is also enabled.