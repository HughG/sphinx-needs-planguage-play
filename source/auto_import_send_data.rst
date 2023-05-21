Auto-Import: Export
====

.. fr:: Once the workflow/session is complete, all suitable generated data will have been exported.
    :id: EG_Session_End_Export_Auto
    :tags: test, tag
    :status: draughty
    :qualifiers: EG_Config_Export_Auto
    :related: EG_Export
    :design_constraints: EG_Export_Auto_NoDelays
    :issues:
        * We changed "any" to "all" and added the word "suitable" to cover the point that we might want to never export certain (auto-)generated types of data from certain apps.
        * Is there an assumption that customers can't set configuration to decide *not* to export specific generated data?
    :priority: :need:`EG_Milestone_AutoImport_MVP`

    The :term:`generated data` may be exported before the session ends, if that is an appropriate implementation.  It should be sent `quickly`.


.. dc:: No undue delays to the export of data.
    :id: EG_Export_Auto_NoDelays
    :priority: :need:`EG_Milestone_AutoImport_MVP`

    Without reference to any specific performance targets, there shall be no undue delays to exporting :term:`generated data` once an application has produced it.


.. fr:: User can confirm that generated data has been queued for export.
    :id: EG_Export_Queue_Status_Visible
    :rationale: If the user cannot see that data is being exported, they may waste time trying to check, or waste time and resources by trying to manually export the data again.
    :priority: :need:`EG_Milestone_AutoImport_MVP`
    :design_ideas: EG_Export_Queue_Status_Display_WorkList, EG_Export_Queue_Status_Display_SessionOverview

    The user must be able to `easily` check that the :term:`generated data` for a study has been queued for export; that the export process is complete or re-trying, when applicable; and whether the export has succeeded, when complete.  The system does *not* need to show the whole queue or any details of it, such as other queue entries, time in queue, etc.

.. di:: Show the status in the :need:`EG_WorkList`.
    :id: EG_Export_Queue_Status_Display_WorkList

.. di:: Show the status in the :need:`EG_Session_Overview`
    :qualifiers: EG_Config_Export_Auto
    :id: EG_Export_Queue_Status_Display_SessionOverview


.. fr:: Source and destination may be different servers, and/or use different protocols, or locators within those protocols.
    :id: EG_Import_Export_Config_Independent
    :issues:
        * This may interact with `EG_Apps_Data_Generated_Reuse`.  We think there may be some apps which generate data which is *only* stored via :term:`StoreX` (i.e., not held in some temp directory by the application) and are needed by that app (or related apps) for later workflow steps.  If the generated series is stored to a completely different server from the origin, and not stored locally anywhere else within :need:`EG`, how could the app access it?  If this is a real scenario, we may need more design here.
    :priority: :need:`EG_Milestone_AutoImport_MVP`


.. fr:: Data can be exported using HTTP PUT, and specifically to Other Product.
    :id: EG_Export_HTTP_PUT_OP
    :rationale: At least one major customer uses :term:`OP`, and supporting it well helps us sell these systems together.
    :priority: :need:`EG_Milestone_AutoImport_MVP`

    The system must be able to export data using at least the aspects of :term:`HTTP PUT` supported by :term:`Other Product`.

.. fr:: test links
    :id: EG_Test_Links
    :author: hughg

    Content with :need:`EG_AutoImport_MissingNeed`.
