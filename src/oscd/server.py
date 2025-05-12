#!/usr/bin/env python3
from fastmcp import FastMCP
from fastmcp.resources import FileResource
from pathlib import Path
from pydantic import AnyUrl

import subprocess
#import os

mcp = FastMCP("OSC MCP Server")

# For now just place the kubeconfig at the ~/.kube/config.
# methods needs to be updated to use the right kubeconfig.
# @mcp.tool()
# def get_kubeconfig() -> str:
#     """Get the kubeconfig file for the Kubernetes or OpenShift cluster.
#
#     First checks if the kubeconfig file exists at the default location.
#     If not, it checks if the KUBECONFIG environment variable is set.
#     If neither is found, it returns an error message.
#     """
#     kubeconfig_path = "~/.kube/config"
#     kubeconfig_path = os.path.expanduser(kubeconfig_path)
#
#     print(f"Checking for kubeconfig at {kubeconfig_path}")
#     if os.path.exists(kubeconfig_path):
#         return kubeconfig_path
#     elif "KUBECONFIG" in os.environ:
#         return os.environ["KUBECONFIG"]
#     else:
#         return "Error: Please set KUBECONFIG environment variable."


@mcp.tool()
def get_cluster_nodes(command: str = "kubectl") -> str:
    """Get the list of nodes in the Kubernetes or OpenShift cluster.

    Args:
        commnand (str): The CLI tool to use ('kubectl' or 'oc').
    """
    if command not in ["kubectl", "oc"]:
        return "Error: Invalid CLI tool specified. Use 'kubectl' or 'oc'."
    return subprocess.run(f"{command} get nodes -o wide",
                          shell=True,
                          capture_output=True,
                          text=True).stdout


@mcp.tool()
def get_installed_operators(command: str = "kubectl") -> str:
    """Get the list  of installed operators in the Kubernetes or OpenShift cluster.

    Args:
        command (str): The CLI tool to use ('kubectl' or 'oc').
    """
    if command not in ["kubectl", "oc"]:
        return "Error: Invalid CLI tool specified. Use 'kubectl' or 'oc'."
    return subprocess.run(f"{command} get csv -A",
                          shell=True,
                          capture_output=True,
                          text=True).stdout


@mcp.tool()
def get_pods(command: str = "kubectl",
             namespace: str = "default") -> str:
    """Get the list of pods in the Kubernetes or OpenShift cluster.

    Args:
        command (str): The CLI tool to use ('kubectl' or 'oc').
        namespace (str): The namespace to query. Or "all" for all namespaces.
    """
    if command not in ["kubectl", "oc"]:
        return "Error: Invalid CLI tool specified. Use 'kubectl' or 'oc'."
    namespace = "--all-namespaces" if namespace == "all" else f"-n {namespace}"

    return subprocess.run(f"{command} get pods {namespace} -o wide",
                          shell=True,
                          capture_output=True,
                          text=True).stdout


@mcp.tool()
def describe_pod(name: str,
                 command: str = "kubectl",
                 namespace: str = "default") -> str:
    """Describe a specific pod in the Kubernetes or OpenShift cluster.

    Args:
        name (str): The name of the pod to describe.
        command (str): The CLI tool to use ('kubectl' or 'oc').
        namespace (str): The namespace of the pod. Or "all" for all namespaces.
    """
    if command not in ["kubectl", "oc"]:
        return "Error: Invalid CLI tool specified. Use 'kubectl' or 'oc'."
    namespace = f"-n {namespace}" if namespace != "all" else ""

    return subprocess.run(f"{command} describe pod {name} {namespace}",
                          shell=True,
                          capture_output=True,
                          text=True).stdout


@mcp.tool()
def get_jobs(command: str = "kubectl",
             namespace: str = "default") -> str:
    """Get the list of jobs in the Kubernetes or OpenShift cluster.

    Args:
        command (str): The CLI tool to use ('kubectl' or 'oc').
        namespace (str): The namespace to query. Or "all" for all namespaces.
    """
    if command not in ["kubectl", "oc"]:
        return "Error: Invalid CLI tool specified. Use 'kubectl' or 'oc'."
    namespace = "--all-namespaces" if namespace == "all" else f"-n {namespace}"

    return subprocess.run(f"{command} get jobs {namespace} -o wide",
                          shell=True,
                          capture_output=True,
                          text=True).stdout


@mcp.tool()
def get_job_logs(name: str,
                 command: str = "kubectl",
                 namespace: str = "default") -> str:
    """Get the logs of a specific job in the Kubernetes or OpenShift cluster.

    Args:
        name (str): The name of the job to get logs for.
        command (str): The CLI tool to use ('kubectl' or 'oc').
        namespace (str): The namespace of the job. Or "all" for all namespaces.
    """
    if command not in ["kubectl", "oc"]:
        return "Error: Invalid CLI tool specified. Use 'kubectl' or 'oc'."
    namespace = f"-n {namespace}" if namespace != "all" else ""

    return subprocess.run(f"{command} logs job/{name} {namespace}",
                          shell=True,
                          capture_output=True,
                          text=True).stdout


@mcp.tool()
def get_daemonsets(command: str = "kubectl",
                   namespace: str = "default") -> str:
    """Get the list of daemonsets in the Kubernetes or OpenShift cluster.

    Args:
        command (str): The CLI tool to use ('kubectl' or 'oc').
        namespace (str): The namespace to query. Or "all" for all namespaces.
    """
    if command not in ["kubectl", "oc"]:
        return "Error: Invalid CLI tool specified. Use 'kubectl' or 'oc'."
    namespace = "--all-namespaces" if namespace == "all" else f"-n {namespace}"

    return subprocess.run(f"{command} get daemonsets {namespace} -o wide",
                          shell=True,
                          capture_output=True,
                          text=True).stdout


@mcp.tool()
def describe_daemonset(name: str,
                       command: str = "kubectl",
                       namespace: str = "default") -> str:
     """Describe a specific daemonset in the Kubernetes or OpenShift cluster.
    
     Args:
          name (str): The name of the daemonset to describe.
          command (str): The CLI tool to use ('kubectl' or 'oc').
          namespace (str): The namespace of the daemonset. Or "all" for all namespaces.
     """
     if command not in ["kubectl", "oc"]:
          return "Error: Invalid CLI tool specified. Use 'kubectl' or 'oc'."
     namespace = f"-n {namespace}" if namespace != "all" else ""
    
     return subprocess.run(f"{command} describe daemonset {name} {namespace} -o json",
                              shell=True,
                              capture_output=True,
                              text=True).stdout


@mcp.tool()
def get_pod_logs(name: str,
                 command: str = "kubectl",
                 namespace: str = "default") -> str:
    """Get the logs of a specific pod in the Kubernetes or OpenShift cluster.

    Args:
        name (str): The name of the pod to get logs for.
        command (str): The CLI tool to use ('kubectl' or 'oc').
        namespace (str): The namespace of the pod. Or "all" for all namespaces.
    """
    if command not in ["kubectl", "oc"]:
        return "Error: Invalid CLI tool specified. Use 'kubectl' or 'oc'."
    namespace = f"-n {namespace}" if namespace != "all" else ""

    return subprocess.run(f"{command} logs {namespace} {name}",
                          shell=True,
                          capture_output=True,
                          text=True).stdout


@mcp.tool()
def get_kataconfig_status(command: str = "kubectl") -> str:
    """Get the status of the KataConfig object in the Kubernetes or OpenShift cluster.

    Args:
        command (str): The CLI tool to use ('kubectl' or 'oc').
    """
    if command not in ["kubectl", "oc"]:
        return "Error: Invalid CLI tool specified. Use 'kubectl' or 'oc'."
    return subprocess.run(f"{command} get kataconfig -o wide",
                          shell=True,
                          capture_output=True,
                          text=True).stdout


@mcp.tool()
def describe_kataconfig(name: str,
                        command: str = "kubectl") -> str:
    """Describe a specific KataConfig object in the Kubernetes or OpenShift cluster.

    Args:
        name (str): The name of the KataConfig object to describe.
        command (str): The CLI tool to use ('kubectl' or 'oc').
    """
    if command not in ["kubectl", "oc"]:
        return "Error: Invalid CLI tool specified. Use 'kubectl' or 'oc'."
    return subprocess.run(f"{command} describe kataconfig {name}",
                          shell=True,
                          capture_output=True,
                          text=True).stdout


@mcp.tool()
def get_configmaps(command: str = "kubectl",
                   namespace: str = "default") -> str:
    """Get the list of configmaps in the Kubernetes or OpenShift cluster.

    Args:
        command (str): The CLI tool to use ('kubectl' or 'oc').
        namespace (str): The namespace to query. Or "all" for all namespaces.
    """
    if command not in ["kubectl", "oc"]:
        return "Error: Invalid CLI tool specified. Use 'kubectl' or 'oc'."
    namespace = "--all-namespaces" if namespace == "all" else f"-n {namespace}"

    return subprocess.run(f"{command} get configmaps {namespace} -o wide",
                          shell=True,
                          capture_output=True,
                          text=True).stdout


@mcp.tool()
def describe_configmap(name: str,
                command: str = "kubectl",
                namespace: str = "default") -> str:
    """Describe a specific configmap in the Kubernetes or OpenShift cluster.

    Args:
        name (str): The name of the configmap to describe.
        command (str): The CLI tool to use ('kubectl' or 'oc').
        namespace (str): The namespace of the configmap. Or "all" for all namespaces.
    """
    if command not in ["kubectl", "oc"]:
        return "Error: Invalid CLI tool specified. Use 'kubectl' or 'oc'."
    namespace = f"-n {namespace}" if namespace != "all" else ""

    return subprocess.run(f"{command} describe configmap {name} {namespace}",
                          shell=True,
                          capture_output=True,
                          text=True).stdout


@mcp.tool()
def get_secrets(command: str = "kubectl",
                namespace: str = "default") -> str:
    """Get the list of secrets in the Kubernetes or OpenShift cluster.

    Args:
        command (str): The CLI tool to use ('kubectl' or 'oc').
        namespace (str): The namespace to query. Or "all" for all namespaces.
    """
    if command not in ["kubectl", "oc"]:
        return "Error: Invalid CLI tool specified. Use 'kubectl' or 'oc'."
    namespace = "--all-namespaces" if namespace == "all" else f"-n {namespace}"

    return subprocess.run(f"{command} get secrets {namespace} -o wide",
                          shell=True,
                          capture_output=True,
                          text=True).stdout

@mcp.tool()
def describe_secret(name: str,
                   command: str = "kubectl",
                   namespace: str = "default") -> str:
    """Describe a specific secret in the Kubernetes or OpenShift cluster.

    Args:
        name (str): The name of the secret to describe.
        command (str): The CLI tool to use ('kubectl' or 'oc').
        namespace (str): The namespace of the secret. Or "all" for all namespaces.
    """
    if command not in ["kubectl", "oc"]:
        return "Error: Invalid CLI tool specified. Use 'kubectl' or 'oc'."
    namespace = f"-n {namespace}" if namespace != "all" else ""

    return subprocess.run(f"{command} describe secret {name} {namespace} -o json",
                          shell=True,
                          capture_output=True,
                          text=True).stdout


user_guide = Path("/tmp/user-guide.txt").resolve()
if user_guide.exists():
    # Use a file:// URI scheme
    readme_resource = FileResource(
        uri=AnyUrl(f"file://{user_guide.as_posix()}"),
        path=user_guide,
        name="OSC 1.9 User guide",
        description="OSC 1.9 user guide for azure only",
        mime_type="text/markdown",
        tags={"documentation", "osc", "userguide", "azure"}
    )
    mcp.add_resource(readme_resource)


if __name__ == "__main__":
    mcp.run(transport="sse")
