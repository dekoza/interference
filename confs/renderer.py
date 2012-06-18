<config>
  <logging level="info">
    <subsystem active="yes" level="debug" name="coherence" />
  <subsystem active="no" level="info" name="webserver" />
  <subsystem active="no" level="info" name="dbus" />
  <subsystem active="yes" level="debug" name="webui" />
  <subsystem active="no" level="info" name="webui_menu_fragment" />
  <subsystem active="no" level="info" name="webui_device_fragment" />
  <subsystem active="no" level="info" name="webui_logging_fragment" />
  <subsystem active="no" level="info" name="ssdp" />
  <subsystem active="no" level="info" name="msearch" />
  <subsystem active="yes" level="debug" name="device" />
  <subsystem active="no" level="info" name="service_server" />
  <subsystem active="no" level="info" name="service_client" />
  <subsystem active="no" level="info" name="action" />
  <subsystem active="no" level="info" name="variable" />
  <subsystem active="no" level="info" name="event_server" />
  <subsystem active="no" level="info" name="event_subscription_server" />
  <subsystem active="no" level="info" name="event_protocol" />
  <subsystem active="yes" level="info" name="soap" />
  <subsystem active="yes" level="debug" name="mediaserver" />
  <subsystem active="yes" level="debug" name="mediarenderer" />
  <subsystem active="no" level="debug" name="controlpoint" />
  <subsystem active="no" level="info" name="connection_manager_server" />
  <subsystem active="no" level="info" name="content_directory_server" />
  <subsystem active="no" level="info" name="ms_client" />
  <subsystem active="no" level="info" name="mr_client" />
  <subsystem active="no" level="info" name="fs_store" />
  <subsystem active="no" level="info" name="fs_item" />
  <subsystem active="no" level="info" name="elisa_player" />
  <subsystem active="yes" level="debug" name="gstreamer_player" />
  <subsystem active="no" level="info" name="iradio_store" />
  <subsystem active="no" level="info" name="iradio_item" />
  <subsystem active="no" level="info" name="axis_cam_store" />
  <subsystem active="no" level="info" name="axis_cam_item" />
  <subsystem active="no" level="info" name="flickr_storage" />
  <subsystem active="no" level="info" name="buzztard_client" />
  <subsystem active="no" level="info" name="buzztard_factory" />
  <subsystem active="no" level="info" name="buzztard_connection" />
  <subsystem active="no" level="info" name="buzztard_item" />
  <subsystem active="no" level="info" name="buzztard_store" />
  <subsystem active="no" level="info" name="buzztard_player" />
  <logfile active="no">/var/log/coherence/renderer.log</logfile>
</logging>
<plugin active="yes">
  <uuid>D10942F0-B798-11E1-B0DD-CDF96088709B</uuid>
  <name>Coherence Audio Player</name>
  <backend>GStreamerPlayer</backend>
</plugin>
<use_dbus>no</use_dbus>
<web-ui>yes</web-ui>
<serverport>30020</serverport>
<interface active="yes">192.168.10.11</interface>
</config>
