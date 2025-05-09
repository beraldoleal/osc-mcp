#!/usr/bin/env python3
from fastmcp import FastMCP
import subprocess
import os

mcp = FastMCP("OSC MCP Server")

@mcp.tool()
def get_kubeconfig() -> str:
    """Get the kubeconfig file for the Kubernetes or OpenShift cluster.

    First checks if the kubeconfig file exists at the default location.
    If not, it checks if the KUBECONFIG environment variable is set.
    If neither is found, it returns an error message.
    """
    kubeconfig_path = "~/.kube/config"
    kubeconfig_path = os.path.expanduser(kubeconfig_path)

    print(f"Checking for kubeconfig at {kubeconfig_path}")
    if os.path.exists(kubeconfig_path):
        return kubeconfig_path
    elif "KUBECONFIG" in os.environ:
        return os.environ["KUBECONFIG"]
    else:
        return "Error: Please set KUBECONFIG environment variable."


@mcp.tool()
def get_cluster_nodes(command: str = "kubectl",
                      kubeconfig: str = "~/.kube/config") -> str:
    """Get the list of nodes in the Kubernetes or OpenShift cluster.

    Args:
        commnand (str): The CLI tool to use ('kubectl' or 'oc').
        kubeconfig (str): The path to the kubeconfig file. Default is ~/.kube/config.
    """
    if command not in ["kubectl", "oc"]:
        return "Error: Invalid CLI tool specified. Use 'kubectl' or 'oc'."
    return subprocess.run(f"{command} get nodes -o wide",
                          shell=True,
                          capture_output=True,
                          text=True).stdout


@mcp.tool()
def get_installed_operators(command: str = "kubectl",
                            kubeconfig: str = "~/.kube/config") -> str:
    """Get the list  of installed operators in the Kubernetes or OpenShift cluster.

    Args:
        command (str): The CLI tool to use ('kubectl' or 'oc').
        kubeconfig (str): The path to the kubeconfig file. Default is ~/.kube/config.
    """
    if command not in ["kubectl", "oc"]:
        return "Error: Invalid CLI tool specified. Use 'kubectl' or 'oc'."
    return subprocess.run(f"{command} get csv -A",
                          shell=True,
                          capture_output=True,
                          text=True).stdout


@mcp.tool()
def get_pods(command: str = "kubectl",
             namespace: str = "default",
             kubeconfig: str = "~/.kube/config") -> str:
    """Get the list of pods in the Kubernetes or OpenShift cluster.

    Args:
        command (str): The CLI tool to use ('kubectl' or 'oc').
        namespace (str): The namespace to query. Or "all" for all namespaces.
        kubeconfig (str): The path to the kubeconfig file. Default is ~/.kube/config.
    """
    if command not in ["kubectl", "oc"]:
        return "Error: Invalid CLI tool specified. Use 'kubectl' or 'oc'."
    namespace = "--all-namespaces" if namespace == "all" else f"-n {namespace}"

    return subprocess.run(f"{command} get pods {namespace} -o wide",
                          shell=True,
                          capture_output=True,
                          text=True).stdout


@mcp.tool()
def get_kataconfig_status(command: str = "kubectl",
                          kubeconfig: str = "~/.kube/config") -> str:
    """Get the status of the KataConfig object in the Kubernetes or OpenShift cluster.

    Args:
        command (str): The CLI tool to use ('kubectl' or 'oc').
        kubeconfig (str): The path to the kubeconfig file. Default is ~/.kube/config.
    """
    if command not in ["kubectl", "oc"]:
        return "Error: Invalid CLI tool specified. Use 'kubectl' or 'oc'."
    return subprocess.run(f"{command} get kataconfig -o wide",
                          shell=True,
                          capture_output=True,
                          text=True).stdout


@mcp.tool()
def describe_kataconfig(name: str,
                        command: str = "kubectl",
                        kubeconfig: str = "~/.kube/config") -> str:
    """Describe a specific KataConfig object in the Kubernetes or OpenShift cluster.

    Args:
        name (str): The name of the KataConfig object to describe.
        command (str): The CLI tool to use ('kubectl' or 'oc').
        kubeconfig (str): The path to the kubeconfig file. Default is ~/.kube/config.
    """
    if command not in ["kubectl", "oc"]:
        return "Error: Invalid CLI tool specified. Use 'kubectl' or 'oc'."
    return subprocess.run(f"{command} describe kataconfig {name}",
                          shell=True,
                          capture_output=True,
                          text=True).stdout

if __name__ == "__main__":
    mcp.run(transport="sse")
