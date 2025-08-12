
:py:mod:`background_process_manager`
====================================

.. py:module:: background_process_manager

Background Process Manager Module.

This module provides a utility for managing long-running background processes
in a shell environment. It handles process spawning, monitoring, and termination,
allowing for safer and more controlled execution of background tasks.

The module is particularly useful for managing persistent services, daemons,
or any long-running commands that need to be started, monitored, and cleanly
terminated programmatically.

.. rubric:: Examples

>>> from haive.tools.toolkits.dev.shell.background_process_manager import BackgroundProcessManager
>>> bg_manager = BackgroundProcessManager()
>>> bg_manager.run_background("npm run dev")
{'success': True, 'pid': 12345, 'message': '✅ npm run dev is running in the background'}
>>> bg_manager.list_running()
[{'pid': 12345, 'command': 'npm run dev', 'status': 'running'}]
>>> bg_manager.stop_process(12345)
{'success': True, 'message': '✅ Process 12345 stopped'}


.. autolink-examples:: background_process_manager
   :collapse:

Classes
-------

.. autoapisummary::

   background_process_manager.BackgroundProcessManager


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BackgroundProcessManager:

   .. graphviz::
      :align: center

      digraph inheritance_BackgroundProcessManager {
        node [shape=record];
        "BackgroundProcessManager" [label="BackgroundProcessManager"];
      }

.. autoclass:: background_process_manager.BackgroundProcessManager
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: background_process_manager
   :collapse:
   
.. autolink-skip:: next
